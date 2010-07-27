from django.conf.urls.defaults import *
import investigation.views as views


urlpatterns = patterns('',
    url(r'^major_to/$', views.major_traffic_offenses, name="major_to"),
    url(r'^minor_to/$', views.minor_traffic_offenses, name="minor_to"),
    url(r'^major_co/$', views.major_criminal_offenses, name="major_co"),
    url(r'^minor_co/$', views.minor_criminal_offenses, name="minor_co"),
    url(r'^co/$', views.criminal_offenses, name="co"),
    url(r'^to/$', views.traffic_offenses, name="to"),
    url(r'^offenses/$', views.offenses, name="offenses"),
)
