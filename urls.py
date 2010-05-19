#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       urls.py

from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^cis/', include('cis.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^$', 'core.views.dashboard', name="homepage"),
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    # Propose to add a regex core to the core urls 
    # (r'^core/', include('cis.core.urls')),
    (r'', include('cis.core.urls')),
)
