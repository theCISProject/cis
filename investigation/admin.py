#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin

from investigation.models import *

admin.site.register(Register)
admin.site.register(Complainant)
admin.site.register(Property)
admin.site.register(Officer)
admin.site.register(Accused)
admin.site.register(Result)
admin.site.register(Forensic)
admin.site.register(ReportBook)
admin.site.register(Remark)
