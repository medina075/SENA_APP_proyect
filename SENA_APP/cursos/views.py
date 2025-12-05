from django.shortcuts import render
from django.template import loader
from .models import Curso
from django.http import HttpResponse

# Create your views here.
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

def details(request, curso_id):
    curso = Curso.objects.get(id=curso_id)
    aprendices_curso = curso.aprendizcurso_set.all()
    instructores_curso = curso.instructorcurso_set.all()
    template = loader.get_template('details.html')
    
    context = {
        'curso': curso,
        'aprendices_curso': aprendices_curso,
        'instructores_curso': instructores_curso,
    }
    
    return HttpResponse(template.render(context, request))