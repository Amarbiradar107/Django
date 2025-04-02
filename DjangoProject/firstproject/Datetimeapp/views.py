from django.shortcuts import render
from django.http import HttpResponse 
import datetime 
# Create your views here.
def date_time(request):
    d = datetime.datetime.now()
    msg = 'Current date time is '+str(d)+' '
    return HttpResponse(msg)