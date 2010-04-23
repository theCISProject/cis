#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin

from cis.locations.models import LocationType, Location

#TODO: Admin customizition for candy eye look.

class LocationTypeAdmin(admin.ModelAdmin):
    pass

class LocationAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent',]
	

admin.site.register(LocationType,LocationTypeAdmin)
admin.site.register(Location,LocationAdmin)
