#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin

from offenses.models import Offense, OffenseCategory

#TODO: Admin customizition for candy eye look.

class OffenseAdmin(admin.ModelAdmin):
    pass

admin.site.register(Offense,OffenseAdmin)
admin.site.register(OffenseCategory)
