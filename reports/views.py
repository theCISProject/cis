from investigation.models import *

from django.http import HttpResponse
from pyofc2  import * 
import random
import time

def chart_data_pie(request):
    t = title(text=time.strftime('%a %Y %b %d'))
    b1 = pie()
    b2 = pie()
    b1.values = range(9,0,-1)
    b2.values = [random.randint(0,9) for i in range(9)]
    b2.colour = '#56acde'
    chart = open_flash_chart()
    chart.title = t    
    chart.add_element(b1)
    chart.add_element(b2)
    return HttpResponse(chart.render())

def chart_data_bar(request):
    t = title(text=time.strftime('%a %Y %b %d'))
    b1 = bar()
    b2 = bar()
    b1.values = range(9,0,-1)
    b2.values = [random.randint(0,9) for i in range(9)]
    b2.colour = '#56acde'
    chart = open_flash_chart()
    chart.title = t    
    chart.add_element(b1)
    chart.add_element(b2)
    return HttpResponse(chart.render())

def chart_data_bar_glass(request):
    t = title(text=time.strftime('%a %Y %b %d'))
    b1 = bar_glass()
    b2 = bar_glass()
    b1.values = range(9,0,-1)
    b2.values = [random.randint(0,9) for i in range(9)]
    b2.colour = '#56acde'
    chart = open_flash_chart()
    chart.title = t    
    chart.add_element(b1)
    chart.add_element(b2)
    return HttpResponse(chart.render())

def chart_data_line(request):
    t = title(text=time.strftime('%a %Y %b %d'))
    b1 = line()
    b2 = line()
    b1.values = range(9,0,-1)
    b2.values = [random.randint(0,9) for i in range(9)]
    b2.colour = '#56acde'
    chart = open_flash_chart()
    chart.title = t    
    chart.add_element(b1)
    chart.add_element(b2)
    return HttpResponse(chart.render())
