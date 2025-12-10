from django import forms
from .models import Curso


class CursoForm(forms.ModelForm):
    """Formulario basado en modelo para crear y editar cursos"""
    
    class Meta:
        model = Curso
        fields = [
            'codigo',
            'nombre',
            'programa',
            'instructor_coordinador',
            'instructores',
            'aprendices',
            'fecha_inicio',
            'fecha_fin',
            'horario',
            'aula',
            'cupos_maximos',
            'estado',
            'observaciones',
        ]
        # Widgets personalizados para mejorar la interfaz en el HTML
        widgets = {
            'codigo': forms.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Código del Curso' }),
            'nombre': forms.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Nombre del Curso' }),
            'programa': forms.Select(attrs={ 'class': 'form-control', 'placeholder': 'Programa de Formación' }),
            'instructor_coordinador': forms.Select(attrs={ 'class': 'form-control', 'placeholder': 'Instructor Coordinador' }),
            'instructores': forms.SelectMultiple(attrs={ 'class': 'form-control', 'placeholder': 'Instructores' }),
            'aprendices': forms.SelectMultiple(attrs={ 'class': 'form-control', 'placeholder': 'Aprendices' }),
            'fecha_inicio': forms.DateInput(attrs={ 'class': 'form-control', 'type': 'date', 'placeholder': 'Fecha Inicio' }),
            'fecha_fin': forms.DateInput(attrs={ 'class': 'form-control', 'type': 'date', 'placeholder': 'Fecha Fin' }),
            'horario': forms.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Horario' }),
            'aula': forms.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Aula/Ambiente' }),
            'cupos_maximos': forms.NumberInput(attrs={ 'class': 'form-control', 'placeholder': 'Cupos Máximos' }),
            'estado': forms.Select(attrs={ 'class': 'form-control', 'placeholder': 'Estado' }),
            'observaciones': forms.Textarea(attrs={ 'class': 'form-control', 'placeholder': 'Observaciones' }),
            
        }
        # Etiquetas personalizadas
        labels = {
            'codigo': 'Código del Curso',
            'nombre': 'Nombre del Curso',
            'programa': 'Programa de Formación',
            'instructor_coordinador': 'Instructor Coordinador',
            'instructores': 'Instructores',
            'aprendices': 'Aprendices',
            'fecha_inicio': 'Fecha Inicio',
            'fecha_fin': 'Fecha Fin',
            'horario': 'Horario',
            'aula': 'Aula/Ambiente',
            'cupos_maximos': 'Cupos Máximos',
            'estado': 'Estado',
            'observaciones': 'Observaciones',            
        }

