#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin

from investigation.models import *

class RegisterAdmin(admin.ModelAdmin):
	list_display=('ir_number','rb_number','complainant','accused','offense')


admin.site.register(Register,RegisterAdmin)
admin.site.register(Complainant)
admin.site.register(Property)
admin.site.register(Officer)
admin.site.register(Accused)
admin.site.register(Result)
admin.site.register(Forensic)
admin.site.register(ReportBook)
admin.site.register(Remark)
