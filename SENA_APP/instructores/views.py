from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Instructor
from django.db.models import Q
from .forms import InstructorForm
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages

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
class InstructorCreateView(generic.CreateView):
    """Vista para crear un nuevo Instructor"""
    model = Instructor
    form_class = InstructorForm
    template_name = 'agregar_Instructor.html'
    success_url = reverse_lazy('instructores:instructores')
    
    def form_valid(self, form):
        """Mostrar mensaje de éxito al crear el Instructor"""
        messages.success(
            self.request,
            f'El Instructor {form.instance.get_full_name()} ha sido registrado exitosamente.'
        )
        return super().form_valid(form)
    
    def form_invalid(self, form):
        """Mostrar mensaje de error si el formulario es inválido"""
        messages.error(
            self.request,
            'Por favor, corrija los errores en el formulario.'
        )
        return super().form_invalid(form)


# UPDATE - Instructor
class InstructorUpdateView(generic.UpdateView):
    """Vista para actualizar un Instructor existente"""
    model = Instructor
    form_class = InstructorForm
    template_name = 'editar_Instructor.html'
    success_url = reverse_lazy('instructores:instructores')
    pk_url_kwarg = 'Instructor_id'
    
    def form_valid(self, form):
        """Mostrar mensaje de éxito al actualizar"""
        messages.success(
            self.request,
            f'El Instructor {form.instance.get_full_name()} ha sido actualizado exitosamente.'
        )
        return super().form_valid(form)
    
    def form_invalid(self, form):
        """Mostrar mensaje de error si el formulario es inválido"""
        messages.error(
            self.request,
            'Por favor, corrija los errores en el formulario.'
        )
        return super().form_invalid(form)


# DELETE - Instructor
class InstructorDeleteView(generic.DeleteView):
    """Vista para eliminar un Instructor"""
    model = Instructor
    template_name = 'eliminar_Instructor.html'
    success_url = reverse_lazy('instructores:instructores')
    pk_url_kwarg = 'Instructor_id'
    
    def delete(self, request, *args, **kwargs):
        """Mostrar mensaje de éxito al eliminar"""
        Instructor = self.get_object()
        messages.success(
            request,
            f'El Instructor {Instructor.get_full_name()} ha sido eliminado exitosamente.'
        )
        return super().delete(request, *args, **kwargs)