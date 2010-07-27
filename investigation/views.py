# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from investigation.models import Register, Offense, OffenseCategory, ReportBook

@login_required()
def major_traffic_offenses(request):
	registers = Register.objects.filter(offense__offense_category__rank=u'MAJOR',
										offense__offense_category__offense_section=u'TRAFFIC')
	context = {
			'registers':registers,
			'full_name':request.user.get_full_name(),
	}
	return render_to_response('reports/major_traffic_offense.html',context,
			context_instance = RequestContext(request),
	)

def minor_traffic_offenses(request):
	registers = Register.objects.filter(offense__offense_category__rank=u'MINOR',
										offense__offense_category__offense_section=u'TRAFFIC')
	context = {
			'registers':registers,
			'full_name':request.user.get_full_name(),
	}
	return render_to_response('reports/minor_traffic_offense.html',context,
			context_instance = RequestContext(request),
	)

def major_criminal_offenses(request):
	registers = Register.objects.filter(offense__offense_category__rank=u'MAJOR',
										offense__offense_category__offense_section=u'CRIMINAL')
	context = {
			'registers':registers,
			'full_name':request.user.get_full_name(),
	}
	return render_to_response('reports/major_criminal_offense.html',context,
			context_instance = RequestContext(request),
	)

def minor_criminal_offenses(request):
	registers = Register.objects.filter(offense__offense_category__rank=u'MINOR',
										offense__offense_category__offense_section=u'CRIMINAL')
	context = {
			'registers':registers,
			'full_name':request.user.get_full_name(),
	}
	return render_to_response('reports/minor_criminal_offense.html',context,
			context_instance = RequestContext(request),
	)

def criminal_offenses(request):
	registers = Register.objects.filter(offense__offense_category__offense_section=u'CRIMINAL')
	context = {
			'registers':registers,
			'full_name':request.user.get_full_name(),
	}
	return render_to_response('reports/criminal_offense.html',context,
			context_instance = RequestContext(request),
	)

def traffic_offenses(request):
	registers = Register.objects.filter(offense__offense_category__offense_section=u'TRAFFIC')
	context = {
			'registers':registers,
			'full_name':request.user.get_full_name(),
	}
	return render_to_response('reports/traffic_offense.html',context,
			context_instance = RequestContext(request),
	)
def offenses(request):
	registers = Register.objects.all()
	context = {
			'registers':registers,
			'full_name':request.user.get_full_name(),
	}
	return render_to_response('reports/offense.html',context,
			context_instance = RequestContext(request),
	)
