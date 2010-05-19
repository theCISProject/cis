#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin

from cis.core.models import Zone, PoliceProfile

#class ZoneAdmin(admin.ModelAdmin):
#	pass

admin.site.register(Zone)
admin.site.register(PoliceProfile)


