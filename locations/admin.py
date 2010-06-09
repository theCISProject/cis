from django.contrib import admin

from locations.models import Station, Country, Region, District, Ward

class StationAdmin(admin.ModelAdmin):
    pass

admin.site.register(Country)
admin.site.register(Ward)
admin.site.register(Region)
admin.site.register(District)
admin.site.register(Station,StationAdmin)
