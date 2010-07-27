from django.contrib.auth.views import login as django_login
from django.contrib.auth.views import logout as django_logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.conf import settings
from django.template import RequestContext
from django.db.models.query_utils import Q
from django.http import HttpResponse
from django.template.loader import render_to_string

from django.contrib.auth.forms import PasswordChangeForm

from core.utils import _get_sort_info
from core.models import StationPolice, PoliceProfile
from locations.models import Station
from investigation.models import Register

@login_required()
def dashboard(request):
    all_offenses = Register.objects.all()
    major_offenses = Register.objects.filter(offense__offense_category__rank=u'MAJOR',)
    minor_offenses = Register.objects.filter(offense__offense_category__rank=u'MINOR',)
    criminal_offenses = Register.objects.filter(offense__offense_category__offense_section=u'CRIMINAL',)
    traffic_offenses = Register.objects.filter(offense__offense_category__offense_section=u'TRAFFIC',)
    
    stations = Station.objects.all()
    context = {
			'all_offenses':all_offenses.count(),
			'major_offenses':major_offenses.count(),
			'minor_offenses':minor_offenses.count(),
			'criminal_offenses':criminal_offenses.count(),
			'traffic_offenses':traffic_offenses.count(),
            'stations' : stations
	}
    
    return render_to_response(
                              "dashboard.html", 
                              context,
                              context_instance = RequestContext(request),
                              )
    
def login(request, template_name="core/login.html"):
    '''Login to cis'''
    # this view, and the one below, is overridden because
    # we need to set the base template to use somewhere
    # somewhere that the login page can access it.
#    request.base_template = settings.BASE_TEMPLATE
    return django_login(request, **{"template_name" : template_name})

def logout(req, template_name="core/loggedout.html"):
    '''Logout of cis'''
#    req.base_template = settings.BASE_TEMPLATE
    return django_logout(req, **{"template_name" : template_name})

@login_required()
def userlist(request):
    template = "core/userlist.html"
    
    columns = (("first_name", "Firstname"),
               ("last_name", "Lastname"),
               ("username", "UserName"),
               ("police_code", "PoliceCode"),
               ("created_date", "Created Date"),
               )

    sort_column, sort_descending = _get_sort_info(request, default_sort_column="first_name",
                                                  default_sort_descending=False)
    sort_desc_string = "-" if sort_descending else ""
    search_string = request.REQUEST.get("q", "")

    query = StationPolice.objects.order_by("%s%s" % (sort_desc_string, sort_column))

    if search_string == "":
        query = query.all()

    else:
        query = query.filter(
           Q(first_name__icontains=search_string) |
           Q(last_name__icontains=search_string))
    
    polices = query
    profiles = PoliceProfile.objects.all()
    
    return render_to_response(template, {"columns": columns,
                                                   "polices": polices,
                                                   "profiles": profiles,
                                                   "sort_column": sort_column,
                                                   "sort_descending": sort_descending,
                                                   "search_string": search_string},
                                                   context_instance = RequestContext(request),
                                                   )

@login_required()
def settings(request):
    return render_to_response(
                              "core/settings.html", 
                              {},
                              context_instance = RequestContext(request),
                              ) 

@login_required()
def edit_profile(request):
    return HttpResponse(" edit profile")

@login_required()
def change_password(request):
    if request.method == 'POST': # If the form has been submitted...
        form = PasswordChangeForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            form.save()
            return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        form = PasswordChangeForm("") # An unbound form

    return render_to_response(
                              "core/change_password.html", 
                              {"form" : form,},
                              context_instance = RequestContext(request),
                              )
