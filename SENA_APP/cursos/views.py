from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Curso
from django.db.models import Q

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def cursos(request):
  mycursos = Curso.objects.all().values()
  template = loader.get_template('all_cursos.html')
  context = {
     'mycursos': mycursos,
     
    }
  return HttpResponse(template.render(context, request))
def details(request, id):
  mycurso = Curso.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mycurso': mycurso,
  }
  return HttpResponse(template.render(context, request))  
