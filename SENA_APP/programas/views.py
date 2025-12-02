from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Programa
from django.db.models import Q

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def programas(request):
  myprogramas = Programa.objects.all().values()
  template = loader.get_template('all_programas.html')
  context = {
     'myprogramas': myprogramas,
     
    }
  return HttpResponse(template.render(context, request))
def details(request, id):
  myprograma = Programa.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'myprograma': myprograma,
  }
  return HttpResponse(template.render(context, request))  