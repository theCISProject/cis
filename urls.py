from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^statics/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_DOC_ROOT}
    ),
    (r'^reports/',include('cis.investigation.urls')),
    (r'^admin/', include(admin.site.urls)),
    url(r'^$', 'core.views.dashboard', name="homepage"),
    (r'', include('cis.core.urls')),
)
# the chart data views
urlpatterns += patterns('reports.views',
    ('^data/pie/$','chart_data_pie'),
    ('^data/bar/$','chart_data_bar'),
    ('^data/barglass/$','chart_data_bar_glass'),
    ('^data/line/$','chart_data_line'),
)
urlpatterns += patterns('',
    (r'^charts/$', 'django.views.generic.simple.direct_to_template', {'template': 'reports/chart.html'}),
)
