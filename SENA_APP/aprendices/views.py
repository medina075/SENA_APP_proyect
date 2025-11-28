from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Aprendiz
from django.db.models import Q

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def aprendices(request):
  myaprendices = Aprendiz.objects.all().values()
  template = loader.get_template('all_aprendices.html')
  context = {
     'myaprendices': myaprendices,
     
    }
  return HttpResponse(template.render(context, request))
def details(request, id):
  myaprendiz = Aprendiz.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'myaprendiz': myaprendiz,
  }
  return HttpResponse(template.render(context, request))  
