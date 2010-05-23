#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django.contrib import admin
from book.models import *
from personal.models import Information

class InformationInline(admin.StackedInline):
	model = Information
	extra = 2

class InformationAdmin(admin.ModelAdmin):
	pass

class DetailInline(admin.TabularInline):
	model = Detail
	extra = 1

class DetailAdmin(admin.ModelAdmin):
	pass

class  ActionInline(admin.TabularInline):
	model = Action
	extra = 1

class ActionAdmin(admin.ModelAdmin):
	pass

class AccusedInline(admin.TabularInline):
	model = Accused
	extra = 1

class AccusedAdmin(admin.ModelAdmin):
	pass

class ArrestInline(admin.TabularInline):
	model = Arrest
	extra = 1

class ArrestAdmin(admin.ModelAdmin):
	pass


class ReportAdmin(admin.ModelAdmin):
	#~ list_display = ('serial_number', 'date', 'time', 'personal_information',
					#~ 'report_detail', 'investigation_number', 'action',
					#~ 'accused', 'arrest', 'property_detail', 'status'
					#~ )
	inlines = [InformationInline, DetailInline, ActionInline, AccusedInline, ArrestInline]
	search_fields = ['serial_number', 'personal_information__name']

admin.site.register(Report,ReportAdmin)
admin.site.register(Arrest,ArrestAdmin)
admin.site.register(Accused,AccusedAdmin)
admin.site.register(Action,ActionAdmin)
admin.site.register(Detail,DetailAdmin)
#~ admin.site.register(Information,InformationAdmin)

