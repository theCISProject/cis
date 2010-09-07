from django import template
from django.conf import settings
from django.utils.safestring import mark_safe

from django.contrib.gis.gdal import OGRGeomType

from geoportal import utils

import random

register = template.Library()


class SafeVariable(template.Variable):

    def resolve(self, context):
        try:
            return super(SafeVariable, self).resolve(context)
        except template.VariableDoesNotExist:
            return self.var


class OptionsNode(template.Node):
    """A template node with a nice option parsing bahaviour."""
    args = 0  # Number of required arguments
    available_options = ()  # List of options the parser should recognize

    def parse_options(self, args):
        self.options = {}
        if len(args) > self.args:
            # Eating empty options, u''
            options = [o for o in ''.join(args[self.args:]).split(',') if o]
            for o in options:
                key, value = o.split('=')
                if not key in self.available_options:
                    raise template.TemplateSyntaxError('"%s" option is not su'
                            'pported. Available options are: %s' % (key,
                            ', '.join(self.available_options)))
                self.options[key] = SafeVariable(value)

    def to_boolean(self, var_name):
        try:
            self.options[var_name] = bool(int(self.options[var_name]))
        except ValueError:
            raise template.TemplateSyntaxError('"%s" can be either 0 or 1 (was'
                ': "%s")' % (var_name, self.options[var_name]))


class MapNode(OptionsNode):
    args = 2
    available_options = ('width', 'height', 'visible', 'color',
                         'opacity', 'zoom', 'navigation')

    def __init__(self, args, var_name=None):
        self.geo_field = template.Variable(args[1])
        self.var_name = var_name
        self.args_ = args

    def render(self, context):
        self.parse_options(self.args_)
        # Generate a probably unique name for javascript variables -- in case
        # there are several maps on a page
        map_var = ''.join(random.sample('abcdefghijklmopqrstuvwxyz', 5))
        map_var = 'map_' + map_var

        # Field type
        geo_field = self.geo_field.resolve(context)
        ftype = geo_field.geom_type.upper()
        is_collection = ftype in ('MULTIPOINT', 'MULTILINESTRING',
                                  'MULTIPOLYGON', 'GEOMETRYCOLLECTION')
        if is_collection:
            if ftype == 'GEOMETRYCOLLECTION':
                collection_type = 'Any'
            else:
                collection_type = OGRGeomType(ftype.replace('MULTI', ''))
        else:
            collection_type = 'None'

        for (key, value) in self.options.items():
            self.options[key] = value.resolve(context)

        # Default options
        if not 'width' in self.options:
            self.options['width'] = utils.DEFAULT_WIDTH

        if not 'height' in self.options:
            self.options['height'] = utils.DEFAULT_HEIGHT

        if not 'color' in self.options:
            self.options['color'] = utils.DEFAULT_COLOR

        if not 'opacity' in self.options:
            self.options['opacity'] = utils.DEFAULT_OPACITY

        self.check_booleans()

        isolated_context = template.Context({
            'options': self.options,
            'api_key': settings.GEOPORTAL_API_KEY,
            'map_var': map_var,
            'is_point': ftype in ('POINT', 'MULTIPOINT'),
            'is_linestring': ftype in ('LINESTRING', 'MULTILINESTRING'),
            'is_polygon': ftype in ('POLYGON', 'MULTIPOLYGON'),
            'is_collection': is_collection,
            'collection_type': collection_type,
            'layers': utils.get_layers((('maps', 1),)),
            'default_lon': utils.DEFAULT_LON,
            'default_lat': utils.DEFAULT_LAT,
            'default_zoom': utils.DEFAULT_ZOOM,
            'point_zoom': utils.POINT_ZOOM,
            'srid': 4326,
            'field_name': ftype.capitalize(),
            'wkt': geo_field.wkt,
            'wms_url': utils.WMS_URL,
        })
        loaded = template.loader.get_template('geoportal/map.html')
        rendered = loaded.render(isolated_context)
        if self.var_name is not None:
            context[self.var_name] = map_var
        return rendered

    def check_booleans(self):
        if not 'visible' in self.options:
            self.options['visible'] = 1
        else:
            self.to_boolean('visible')

        if 'navigation' in self.options:
            self.to_boolean('navigation')


@register.tag
def geoportal_map(parser, token):
    """
    {% geoportal_map field option1=value1, option2=value2, ... %}

    Renders a geographic field (point, polygon, path...)

    Options:             Default
     * width (pixels)    400
     * height (pixels)   300
     * visible (1|0)     1
     * color (rrggbb)    ee9900 (OpenLayers.Feature.Vector
                                 .style["default"]["fillColor"])
     * opacity (0 -> 1)  0.4
     * zoom (~3 -> 14)   if not provided, calculated automatically
     * navigation (1|0)  turn navigation on
    """
    bits = token.split_contents()
    if len(bits) < 2:
        raise template.TemplateSyntaxError('geoportal_map takes at least one '
                                           'argument')
    if len(bits) > 3 and bits[-2] == 'as':
        return MapNode(bits[:-2], var_name=bits[-1])
    return MapNode(bits)


@register.simple_tag
def geoportal_js():
    return mark_safe('<script type="text/javascript" src=' + \
                     '"%sGeoportalExtended.js"></script>' % utils.MEDIA_URL)


class GmlNode(OptionsNode):
    args = 3
    available_options = ('color', 'opacity', 'width', 'extract',
                         'focus', 'popup')
    format_type = None
    force_style = False

    def __init__(self, args):
        self.map_var = template.Variable(args[1])
        self.kml_url = SafeVariable(args[2])
        self.parse_options(args)

    def render(self, context):
        for key, value in self.options.items():
            self.options[key] = value.resolve(context)

        if self.force_style:
            self.options['extract'] = True
            self.options['style'] = True
        else:
            if 'extract' in self.options:
                self.to_boolean('extract')
            else:
                self.options['extract'] = True

            for key in ('width', 'opacity', 'color'):
                # Setting any of those disables style extraction
                if key in self.options:
                    self.options['extract'] = False
                    break

        if not 'width' in self.options:
            self.options['width'] = 2

        if not 'opacity' in self.options:
            if self.format_type == 'gpx':
                self.options['opacity'] = 1
            else:
                self.options['opacity'] = utils.DEFAULT_OPACITY

        if not 'color' in self.options:
            self.options['color'] = utils.DEFAULT_COLOR

        if 'focus' in self.options:
            self.to_boolean('focus')
        else:
            self.options['focus'] = True

        if 'popup' in self.options:
            self.to_boolean('popup')
        else:
            self.options['popup'] = True

        self.options['url'] = self.kml_url.resolve(context)
        self.options['map_var'] = self.map_var.resolve(context)
        self.options['format'] = self.format_type
        return template.loader.render_to_string('geoportal/gml.html',
                                                self.options)


class KmlNode(GmlNode):
    format_type = 'kml'


@register.tag
def geoportal_kml(parser, token):
    """Adds a layer to an existing map from a KML file
    {% geoportal_kml map_var kml_url color=..., width=..., opacity=... %}

    Options all have default values:
        color: utils.DEFAULT_COLOR
        width: 2
        opacity: utils.DEFAULT_OPACITY
        extract: 1
    """
    bits = token.split_contents()
    if len(bits) < 3:
        raise template.TemplateSyntaxError('geoportal_kml takes at least two '
                                           'arguments')
    return KmlNode(bits)


class GpxNode(GmlNode):
    format_type = 'gpx'
    force_style = True
    available_options = ('color', 'opacity', 'width', 'focus', 'popup')


@register.tag
def geoportal_gpx(parser, token):
    """Same as KML, renders a GPX file.
    Options (defaut value):
        width: width of the feature (2)
        opacity: stroke opacity (1)
        color: feature color (utils.DEFAULT_COLOR)
    """
    bits = token.split_contents()
    if len(bits) < 3:
        raise template.TemplateSyntaxError('geoportal_gpx takes at least two '
                                           'arguments')
    return GpxNode(bits)
