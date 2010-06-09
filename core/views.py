from django.contrib.auth.views import login as django_login
from django.contrib.auth.views import logout as django_logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.conf import settings
from django.template import RequestContext

@login_required()
def dashboard(request):
    return render_to_response(
                              "dashboard.html", 
                              {},
                              context_instance = RequestContext(request),
                              )
    
def login(request, template_name="core/login.html"):
    '''Login to cis'''
    # this view, and the one below, is overridden because
    # we need to set the base template to use somewhere
    # somewhere that the login page can access it.
    request.base_template = settings.BASE_TEMPLATE
    return django_login(request, **{"template_name" : template_name})

def logout(req, template_name="core/loggedout.html"):
    '''Logout of cis'''
    req.base_template = settings.BASE_TEMPLATE
    return django_logout(req, **{"template_name" : template_name})