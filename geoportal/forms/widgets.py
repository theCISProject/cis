from django.conf import settings
from django.contrib.gis import forms
from django.template import loader

from geoportal import utils


class BaseWidget(forms.Textarea):
    template = 'geoportal/widget.html'
    is_point = False
    is_linestring = False
    is_polygon = False
    is_collection = False
    collection_type = 'None'

    def __init__(self, *args, **kwargs):
        super(BaseWidget, self).__init__(*args, **kwargs)
        attrs = kwargs.pop('attrs', {})
        self.options = {
            'width': attrs.pop('width', utils.DEFAULT_WIDTH),
            'height': attrs.pop('height', utils.DEFAULT_HEIGHT),
            'color': attrs.pop('color', utils.DEFAULT_COLOR),
            'opacity': attrs.pop('opacity', utils.DEFAULT_OPACITY),
            'default_zoom': attrs.pop('default_zoom', utils.DEFAULT_ZOOM),
            'default_lon': attrs.pop('default_lon', utils.DEFAULT_LON),
            'default_lat': attrs.pop('default_lat', utils.DEFAULT_LAT),
            'layers': utils.get_layers(attrs.pop('layers', (('maps', 1),))),
            'srid': attrs.pop('srid', 4326),
        }

    def render(self, name, value, attrs=None):
        if value is None:
            value = ''

        context = {
            'map_var': 'map_' + name,
            'is_polygon': self.is_polygon,
            'is_linestring': self.is_linestring,
            'is_point': self.is_point,
            'is_collection': self.is_collection,
            'collection_type': self.collection_type,
            'api_key': settings.GEOPORTAL_API_KEY,
            'wms_url': utils.WMS_URL,
            'field_name': name,
            'wkt': value,
            'point_zoom': utils.POINT_ZOOM,
            'admin_media_url': settings.ADMIN_MEDIA_PREFIX,
        }
        context.update(self.options)

        return loader.render_to_string(self.template, context)


class PointWidget(BaseWidget):
    is_point = True


class MultiPointWidget(PointWidget):
    is_collection = True
    collection_type = 'MultiPoint'


class LineStringWidget(BaseWidget):
    is_linestring = True


class MultiLineStringWidget(LineStringWidget):
    is_collection = True
    collection_type = 'MultiLineString'


class PolygonWidget(BaseWidget):
    is_polygon = True


class MultiPolygonWidget(PolygonWidget):
    is_collection = True
    collection_type = 'MultiPolygon'
