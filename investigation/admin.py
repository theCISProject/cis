#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin

from investigation.models import *

class RegisterAdmin(admin.ModelAdmin):
	list_display=('reportbook','complainant','accused','offense','results')
	list_filter=('reportbook','offense',)
	list_per_page=50
	search_fields=['reportbook__ir_number','offense__offense_title',
				'offense__offense_category',]

class AccusedAdmin(admin.ModelAdmin):
	list_display=('first_name','last_name','age','gender','nationality')
	search_fields=['first_name','last_name','age','gender','nationality']

class ReportBookAdmin(admin.ModelAdmin):
	list_display=('station','ir_number')
	search_fields=['station__name','ir_number']
	#list_filter=('station','ir_number',)

class ComplainantAdmin(admin.ModelAdmin):
	list_display=('first_name','last_name','age','occupation')
	search_fields=['first_name','last_name','age','occupation']

class ForensicAdmin(admin.ModelAdmin):
	list_display=('tcro_number','dispatch_date','return_date')
	search_fields=['tcro_number']

class OfficerAdmin(admin.ModelAdmin):
	list_display=('first_name','last_name','position')
	search_fields=['first_name','last_name','position']

class PropertyAdmin(admin.ModelAdmin):
	list_display=('stollen','recovered')
	search_fields=['stollen','recovered']

class ResultAdmin(admin.ModelAdmin):
	list_display=('explanation','date')
	search_fields=['explation']

class RemarkAdmin(admin.ModelAdmin):
	list_display=('description',)
	search_fields=['description',]

admin.site.register(Register,RegisterAdmin)
admin.site.register(Complainant,ComplainantAdmin)
admin.site.register(Property,PropertyAdmin)
admin.site.register(Officer,OfficerAdmin)
admin.site.register(Accused,AccusedAdmin)
admin.site.register(Result,ResultAdmin)
admin.site.register(Forensic,ForensicAdmin)
admin.site.register(ReportBook,ReportBookAdmin)
admin.site.register(Remark,RemarkAdmin)
