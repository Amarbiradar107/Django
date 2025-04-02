from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def display_test(request):
        s = "<b>Test App</b>"
        return HttpResponse(s)