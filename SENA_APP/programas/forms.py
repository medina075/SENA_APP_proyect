from django import forms
from .models import Programa


class ProgramaForm(forms.ModelForm):
    """Formulario basado en modelo para crear y editar programas"""
    
    class Meta:
        model = Programa
        fields = [
            'codigo',
            'nombre',
            'nivel_formacion',
            'modalidad',
            'duracion_meses',
            'duracion_horas',
            'descripcion',
            'competencias',
            'perfil_egreso',
            'requisitos_ingreso',
            'centro_formacion',
            'regional',
            'estado',
        ]
        # Widgets personalizados para mejorar la interfaz en el HTML
        widgets = {
            'codigo': forms.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Código del Programa' }),
            'nombre': forms.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Nombre del Programa' }),
            'nivel_formacion': forms.Select(attrs={ 'class': 'form-control', 'placeholder': 'Nivel de Formación' }),
            'modalidad': forms.Select(attrs={ 'class': 'form-control', 'placeholder': 'Modalidad' }),
            'duracion_meses': forms.NumberInput(attrs={ 'class': 'form-control', 'placeholder': 'Duración en Meses' }),
            'duracion_horas': forms.NumberInput(attrs={ 'class': 'form-control', 'placeholder': 'Duración en Horas' }),
            'descripcion': forms.Textarea(attrs={ 'class': 'form-control', 'placeholder': 'Descripción del Programa' }),
            'competencias': forms.Textarea(attrs={ 'class': 'form-control', 'placeholder': 'Competencias a Desarrollar' }), 
            'perfil_egreso': forms.Textarea(attrs={ 'class': 'form-control', 'placeholder': 'Perfil de Egreso' }),
            'requisitos_ingreso': forms.Textarea(attrs={ 'class': 'form-control', 'placeholder': 'Requisitos de Ingreso' }),
            'centro_formacion': forms.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Centro de Formación' }),
            'regional': forms.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Regional' }),
            'estado': forms.Select(attrs={ 'class': 'form-control', 'placeholder': 'Estado' }),
        }
        # Etiquetas personalizadas
        labels = {
            'codigo': 'Código del Programa',
            'nombre': 'Nombre',
            'nivel_formacion': 'Nivel de Formación',
            'modalidad': 'Modalidad',
            'duracion_meses': 'Duración en Meses',
            'duracion_horas': 'Duración en Horas',
            'descripcion': 'Descripción del Programa',
            'competencias': 'Competencias a Desarrollar',
            'perfil_egreso': 'Perfil de Egreso',
            'requisitos_ingreso': 'Requisitos de Ingreso',
            'centro_formacion': 'Centro de Formación',
            'regional': 'Regional',
            'estado': 'Estado',
        }


    
  
