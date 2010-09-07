from django.conf import settings

POINT_ZOOM = getattr(settings, 'GEOPORTAL_POINT_ZOOM', 14)
DEFAULT_LON = getattr(settings, 'GEOPORTAL_DEFAULT_LON', 2)
DEFAULT_LAT = getattr(settings, 'GEOPORTAL_DEFAULT_LAT', 47)
DEFAULT_ZOOM = getattr(settings, 'GEOPORTAL_DEFAULT_ZOOM', 5)
DEFAULT_WIDTH = getattr(settings, 'GEOPORTAL_DEFAULT_WIDTH', 600)
DEFAULT_HEIGHT = getattr(settings, 'GEOPORTAL_DEFAULT_HEIGHT', 400)
DEFAULT_COLOR = getattr(settings, 'GEOPORTAL_DEFAULT_COLOR', 'ee9900')
DEFAULT_OPACITY = getattr(settings, 'GEOPORTAL_DEFAULT_OPACITY', 0.4)
MEDIA_URL = getattr(settings, 'GEOPORTAL_MEDIA_URL',
                              'http://api.ign.fr/geoportail/api/js/1.0/')

LAYERS = {
    # See https://api.ign.fr/geoportail/api/doc/fr/webmaster/layers.html
    # for an explanation of the meaning of each layer.

    # The layers can or cannot be accessed depending on your API contract.
    'photos': 'ORTHOIMAGERY.ORTHOPHOTOS:WMSC',
    'maps': 'GEOGRAPHICALGRIDSYSTEMS.MAPS:WMSC',
    'terrain': 'ELEVATION.SLOPS',
    'cadaster': 'CADASTRALPARCELS.PARCELS',
    'hydrography': 'HYDROGRAPHY.HYDROGRAPHY',
    'roads': 'TRANSPORTNETWORKS.ROADS',
    'railways': 'TRANSPORTNETWORKS.RAILWAYS',
    'runways': 'TRANSPORTNETWORKS.RUNWAYS',
    'buildings': 'BUILDINGS.BUILDINGS',
    'gov': 'UTILITYANDGOVERNMENTALSERVICES.ALL',
    'boundaries': 'ADMINISTRATIVEUNITS.BOUNDARIES',
    'coast': 'SEAREGIONS.LEVEL0',
}

WMS_URL = 'http://wxs.ign.fr/geoportail/wmsc'


def get_layers(layers):
    """
    A helper that returns all the information needed to display a (set of)
    layer(s) in a template
    """
    lyrs = []
    for (key, value) in layers:
        lyrs.append({
            'switcher_name': key.capitalize(),
            'name': LAYERS[key],
            'resource_name': LAYERS[key].split(':')[0],
            'opacity': str(value),
        })
    return lyrs
