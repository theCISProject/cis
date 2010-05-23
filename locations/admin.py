#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin

from locations.models import LocationType, Location, Station

#TODO: Admin customizition for candy eye look.

class LocationTypeAdmin(admin.ModelAdmin):
    pass

class LocationAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent',]

class StationAdmin(admin.ModelAdmin):
    pass

admin.site.register(LocationType,LocationTypeAdmin)
admin.site.register(Location,LocationAdmin)
admin.site.register(Station,StationAdmin)
