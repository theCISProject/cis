from django.conf.urls.defaults import *
from django.conf import settings


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^statics/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_DOC_ROOT}),
    url(r'^$', 'core.views.dashboard', name="homepage"),
    (r'^admin/', include(admin.site.urls)),
    (r'', include('cis.core.urls')),
)
