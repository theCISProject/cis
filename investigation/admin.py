#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin

from investigation.models import *

class RegisterAdmin(admin.ModelAdmin):
	list_display=('ir_number','reportbook','complainant','accused','offense')
	list_filter=('reportbook','offense',)
	list_per_page=50
	search_fields=['offense__offense_title','offense__offense_category']

class AccusedAdmin(admin.ModelAdmin):
	list_display=('first_name','last_name','age','gender','nationality')


admin.site.register(Register,RegisterAdmin)
admin.site.register(Complainant)
admin.site.register(Property)
admin.site.register(Officer)
admin.site.register(Accused,AccusedAdmin)
admin.site.register(Result)
admin.site.register(Forensic)
admin.site.register(ReportBook)
admin.site.register(Remark)
