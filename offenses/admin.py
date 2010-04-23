#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin

from cis.offenses.models import Offense, Category

#TODO: Admin customizition for candy eye look.

class OffenseAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass
	

admin.site.register(Offense,OffenseAdmin)
admin.site.register(Category,CategoryAdmin)
