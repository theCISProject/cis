from django.conf.urls.defaults import *
import investigation.views as views


urlpatterns = patterns('',
    url(r'^mto/$', views.major_traffic_offenses, name="mto"),
)
