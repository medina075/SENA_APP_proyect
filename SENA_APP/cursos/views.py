from django.shortcuts import render
from django.template import loader
from .models import Curso
from django.http import HttpResponse
from django.db.models import Q
from .forms import CursoForm
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.
def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())
def cursos(request):
    mycursos = Curso.objects.all()
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
class CursoCreateView(generic.CreateView):
    """Vista para crear un nuevo curso"""
    model = Curso
    form_class = CursoForm
    template_name = 'agregar_curso.html'
    success_url = reverse_lazy('cursos:cursos')
    
    def form_valid(self, form):
        """Mostrar mensaje de éxito al crear el curso"""
        messages.success(
            self.request,
            f'El curso {form.instance.get_full_name()} ha sido registrado exitosamente.'
        )
        return super().form_valid(form)
    
    def form_invalid(self, form):
        """Mostrar mensaje de error si el formulario es inválido"""
        messages.error(
            self.request,
            'Por favor, corrija los errores en el formulario.'
        )
        return super().form_invalid(form)


# UPDATE - curso
class CursoUpdateView(generic.UpdateView):
    """Vista para actualizar un curso existente"""
    model = Curso
    form_class = CursoForm
    template_name = 'editar_curso.html'
    success_url = reverse_lazy('cursos:cursos')
    pk_url_kwarg = 'curso_id'
    
    def form_valid(self, form):
        """Mostrar mensaje de éxito al actualizar"""
        messages.success(
            self.request,
            f'El curso {form.instance.get_full_name()} ha sido actualizado exitosamente.'
        )
        return super().form_valid(form)
    
    def form_invalid(self, form):
        """Mostrar mensaje de error si el formulario es inválido"""
        messages.error(
            self.request,
            'Por favor, corrija los errores en el formulario.'
        )
        return super().form_invalid(form)


# DELETE - curso
class CursoDeleteView(generic.DeleteView):
    """Vista para eliminar un curso"""
    model = Curso
    template_name = 'eliminar_curso.html'
    success_url = reverse_lazy('cursos:cursos')
    pk_url_kwarg = 'curso_id'
    
    def delete(self, request, *args, **kwargs):
        """Mostrar mensaje de éxito al eliminar"""
        curso = self.get_object()
        messages.success(
            request,
            f'El curso {curso.get_full_name()} ha sido eliminado exitosamente.'
        )
        return super().delete(request, *args, **kwargs)