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
from cis.personal.models import Information

class InformationAdmin(admin.ModelAdmin):
#        fieldsets = (
#            (None , {
#                    'fields' : ('name', 'sex', 'age')}),
#        )
	list_display = ('name', 'sex', 'age', 'nationality', 'occupation',
					'phone_number', 'e_mail', 'voter_id')

admin.site.register(Information,InformationAdmin)
