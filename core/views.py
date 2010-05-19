from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.decorators.cache import cache_page
from django.contrib.auth.views import login as django_login
from django.contrib.auth.views import logout as django_logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import *

from django.shortcuts import render_to_response
from cis.core import settings

@login_required()
def dashboard(req):
    dashboard = """
        <html>
            <title>
                <head>Dashboard</head>
            </title>

            <body>
                <h1>This is Dashboard</h1>
                <p>
                    Allen: Got some problems with linking css and tamplates inheritance.. look into it.!
                </p>
                <a href="/accounts/logout">Logout</a>
            </body>
        </html>
    """
    return HttpResponse(dashboard)
#    return render_to_response(req, "dashboard.html")
    
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

# username = request.POST['username']
#    password = request.POST['password']
#    user = authenticate(username=username, password=password)
#    if user is not None:
#        if user.is_active:
#            login(request, user)
#            # Redirect to a success page.
#        else:
#            # Return a 'disabled account' error message
#    else:
#        # Return an 'invalid login' error message.