from django.contrib import admin

from locations.models import Station, Country, Region, District

class StationAdmin(admin.ModelAdmin):
    pass

admin.site.register(Country)
admin.site.register(Region)
admin.site.register(District)
admin.site.register(Station,StationAdmin)