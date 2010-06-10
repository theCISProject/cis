from django.contrib import admin

from locations.models import Station, Country, Region, District, Ward


class CountryAdmin(admin.ModelAdmin):
	list_display=('name','code')

class RegionAdmin(admin.ModelAdmin):
	list_display=('name','code','country')

class DistrictAdmin(admin.ModelAdmin):
	list_display=('name','code','region')

class WardAdmin(admin.ModelAdmin):
	list_display=('name','code','district')	

class StationAdmin(admin.ModelAdmin):
    list_display=('name','code','ward','zone')

admin.site.register(Country,RegionAdmin)
admin.site.register(Ward,WardAdmin)
admin.site.register(Region,RegionAdmin)
admin.site.register(District,DistrictAdmin)
admin.site.register(Station,StationAdmin)
