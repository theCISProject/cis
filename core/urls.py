from django.conf.urls.defaults import *
import core.views as views

from django.conf import settings
    
urlpatterns = patterns('',
    url(r'^dashboard/$',     views.dashboard, name="dashboard"),
    url(r'^accounts/login/$', views.login, {"template_name": settings.LOGIN_TEMPLATE }, name="login"),
    url(r'^accounts/logout/$', views.logout, {"template_name": settings.LOGGEDOUT_TEMPLATE }, name="logout"),
)