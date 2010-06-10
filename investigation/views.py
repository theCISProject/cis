# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from investigation.models import Register, Offense, OffenseCategory, ReportBook

def major_traffic_offenses(request):
	registers = Register.objects.filter(offense__offense_category__rank=u'MAJ')
	context = {
			'registers':registers,
			'full_name':request.user.get_full_name(),
	}
	return render_to_response('reports/major_traffic_offense.html',context,
			context_instance = RequestContext(request),
	)
