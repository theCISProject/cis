#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin

from offenses.models import Offense, OffenseCategory

#TODO: Admin customizition for candy eye look.

class OffenseCategoryAdmin(admin.ModelAdmin):
	list_display=('category_name','rank','offense_section')

class OffenseAdmin(admin.ModelAdmin):
    list_display=('offense_title','offense_category')

admin.site.register(Offense,OffenseAdmin)
admin.site.register(OffenseCategory,OffenseCategoryAdmin)
