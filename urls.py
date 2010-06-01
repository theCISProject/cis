#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       urls.py
from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^cis/', include('cis.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^statics/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_DOC_ROOT}),
    url(r'^$', 'core.views.dashboard', name="homepage"),
    (r'^admin/', include(admin.site.urls)),
    # Propose to add a regex core to the core urls 
    # (r'^core/', include('cis.core.urls')),
    (r'', include('cis.core.urls')),
)
