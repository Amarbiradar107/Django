from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Person

def add_person(request):
    person = Person(name="Alice", age=30)
    person.save()
    return HttpResponse("Person added!")