from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^statics/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_DOC_ROOT}),
    (r'^admin/', include(admin.site.urls)),
    url(r'^$', 'core.views.dashboard', name="homepage"),
    (r'', include('cis.core.urls')),
)
