#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin

from cis.investigation.models import Evidence, Book

class EvidenceAdmin(admin.ModelAdmin):
	pass

class BookAdmin(admin.ModelAdmin):
	pass
	

admin.site.register(Evidence,EvidenceAdmin)
admin.site.register(Book,BookAdmin)
