#from django.http import HttpResponse
#from django.http import HttpResponseRedirect
#from django.views.decorators.cache import cache_page
from django.contrib.auth.views import login as django_login
from django.contrib.auth.views import logout as django_logout
from django.contrib.auth.decorators import login_required
#from django.core.exceptions import *
from django.shortcuts import render_to_response
# from cis.core import settings #depretiated soon to be completely removed.
from django.conf import settings

@login_required()
def dashboard(req):
    return render_to_response("dashboard.html", {})
    
def login(request, template_name="core/login.html"):
    '''Login to rapidsms'''
    # this view, and the one below, is overridden because
    # we need to set the base template to use somewhere
    # somewhere that the login page can access it.
    request.base_template = settings.BASE_TEMPLATE
    return django_login(request, **{"template_name" : template_name})

def logout(req, template_name="core/loggedout.html"):
    '''Logout of rapidsms'''
    req.base_template = settings.BASE_TEMPLATE
    return django_logout(req, **{"template_name" : template_name})