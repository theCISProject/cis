#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       admin.py
#       
#       Copyright 2010 Crime information system
#		John Francis Mukulu		<john.f.mukulu@gmail.com>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

from django.contrib import admin
from cis.book.models import *
from cis.personal.models import Information

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

