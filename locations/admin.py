from django.contrib.gis import admin
from django.contrib.gis.maps.google import GoogleMap

from locations.models import Country, Region, District, Ward, Station

#TODO: open a google account for cis, for maps, email,
GMAP = GoogleMap(key='abcdefg') # Can also set GOOGLE_MAPS_API_KEY in settings

class GoogleAdmin(admin.OSMGeoAdmin):
    extra_js = [GMAP.api_url + GMAP.key]
    map_template = 'gis/admin/google.html'
    
admin.site.register(Station, GoogleAdmin)
admin.site.register(Country)
admin.site.register(Region)
admin.site.register(District)
admin.site.register(Ward)