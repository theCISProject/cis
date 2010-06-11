from django.contrib.auth.views import login as django_login
from django.contrib.auth.views import logout as django_logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.conf import settings
from django.template import RequestContext
from django.template.loader import render_to_string

from locations.models import Station

@login_required()
def map_index(req):
    stations = Station.objects.all()
    return render_to_response(req,'locations/index.html', {
        'stations': stations,
        'content': render_to_string('locations/stations.html', {'stations':stations}),
    })
