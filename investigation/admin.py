#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin

from cis.investigation.models import *

admin.site.register(Register)
admin.site.register(Complainant)
admin.site.register(Property)
admin.site.register(Officer)
admin.site.register(Accused)
admin.site.register(Result)
