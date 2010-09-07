from django.contrib.gis.admin import site, GeoModelAdmin
from django.conf import settings

from geoportal import utils

if not hasattr(settings, 'GEOPORTAL_API_KEY'):
    # Just raising a warning, it's not fatal after all
    import warnings
    warnings.warn("GEOPORTAL_API_KEY could not be found in your settings. "
                  "It is necessary to get maps to work.")


class GeoPortalAdmin(GeoModelAdmin):
    """A base model for displaying a GeoPortal admin map"""
    ##############
    # Public API #
    ##############

    map_width = utils.DEFAULT_WIDTH  # Dimensions of the
    map_height = utils.DEFAULT_HEIGHT # map (pixels)

    max_zoom = 20    # Zoom levels: 20 = finest
    min_zoom = 0     #               0 = world
    point_zoom = utils.POINT_ZOOM  # Default zoom level for a single point

    default_zoom = 5 # display a whole country

    default_lon = 2  # Default location
    default_lat = 47 # is France

    # Show map info or not
    map_info = False

    # Layers
    layers = (
        # ('code', opacity),
        # Order matters, layers are added in this order.
        #('photos', 1),
        ('maps', 1),
    )

    # Display the layer switcher
    layerswitcher = True

    ###############
    # Private API #
    ###############
    map_template = 'gis/admin/geoportal.html'
    wms_url = utils.WMS_URL
    openlayers_url = utils.MEDIA_URL + 'GeoportalExtended.js'

    # Mouse position: already displayed by Geoportail
    mouse_position = False
    # Same for scale
    scale_text = False

    def get_map_widget(self, db_field):
        widget = super(GeoPortalAdmin, self).get_map_widget(db_field)
        widget.params['map_info'] = self.map_info
        widget.params['layers'] = utils.get_layers(self.layers)
        widget.params['api_key'] = settings.GEOPORTAL_API_KEY
        widget.params['feature_color'] = utils.DEFAULT_COLOR
        widget.params['feature_opacity'] = utils.DEFAULT_OPACITY
        return widget
