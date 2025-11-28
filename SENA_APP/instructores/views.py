from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Instructor
from django.db.models import Q

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def instructores(request):
  myinstructores = Instructor.objects.all().values()
  template = loader.get_template('all_instructores.html')
  context = {
     'myinstructores': myinstructores,
     
    }
  return HttpResponse(template.render(context, request))
def details(request, id):
  myinstructor = Instructor.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'myinstructor': myinstructor,
  }
  return HttpResponse(template.render(context, request))  