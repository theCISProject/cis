#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django.contrib import admin
from book.models import *


class DetailAdmin(admin.ModelAdmin):
	pass


class ActionAdmin(admin.ModelAdmin):
	pass

class AccusedAdmin(admin.ModelAdmin):
	pass

class ArrestAdmin(admin.ModelAdmin):
	list_display = ('report','name',
					'status',
					)
	search_fields = ['status','name']

class InformationAdmin(admin.ModelAdmin):
	pass
class ReportAdmin(admin.ModelAdmin):
	list_display = ('serial_number', 'investigation_number', 'property_detail',
					'status',
					)
	search_fields = ['serial_number','investigation_number','property_detail']

admin.site.register(Report,ReportAdmin)
admin.site.register(Arrest,ArrestAdmin)
admin.site.register(Accused,AccusedAdmin)
admin.site.register(Action,ActionAdmin)
admin.site.register(Detail,DetailAdmin)
admin.site.register(Information,InformationAdmin)

