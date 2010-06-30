from django.conf.urls.defaults import *
import core.views as views

from django.conf import settings
    
urlpatterns = patterns('',
    url(r'^dashboard/$',     views.dashboard, name="dashboard"),
    url(r'^accounts/login/$', views.login, {"template_name": settings.LOGIN_TEMPLATE }, name="login"),
    url(r'^accounts/logout/$', views.logout, {"template_name": settings.LOGGEDOUT_TEMPLATE }, name="logout"),
    url(r'^core/userlist$',     views.userlist, name="userlist"),
    url(r'^core/settings$',     views.settings, name="settings"),
    url(r'^settings/password$', views.change_password, name="change_password"),
    url(r'^settings/profile$', views.edit_profile, name="edit_profile"),
)