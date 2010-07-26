from django.contrib.gis import admin
from django.contrib.gis.maps.google import GoogleMap

from locations.models import Country, Region, District, Ward, Station

#TODO: open a google account for cis, for maps, email,
GMAP = GoogleMap(key='abcdefg') # Can also set GOOGLE_MAPS_API_KEY in settings

class GoogleAdmin(admin.OSMGeoAdmin):
    extra_js = [GMAP.api_url + GMAP.key]
    map_template = 'gis/admin/google.html'
    list_display=('name','code','added_date','modified_date')
    search_fields=['name','code']

class CountryAdmin(admin.ModelAdmin):
	list_display=('name','code','added_date','modified_date')
	search_fields=['name','code']

class RegionAdmin(admin.ModelAdmin):
	list_display=('name','country','code','added_date','modified_date',)
	search_fields=['name','code']

class DistrictAdmin(admin.ModelAdmin):
	list_display=('name','region','code','added_date','modified_date',)
	search_fields=['name','code']

class WardAdmin(admin.ModelAdmin):
	list_display=('name','district','code','added_date','modified_date',)
	search_fields=['name','code']

admin.site.register(Station, GoogleAdmin)
admin.site.register(Country,CountryAdmin)
admin.site.register(Region,RegionAdmin)
admin.site.register(District,DistrictAdmin)
admin.site.register(Ward,WardAdmin)
