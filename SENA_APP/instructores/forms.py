from django import forms
from .models import Instructor


class InstructorForm(forms.ModelForm):
    """Formulario basado en modelo para crear y editar instructores"""
    
    class Meta:
        model = Instructor
        fields = [
            'documento_identidad',
            'tipo_documento',
            'nombre',
            'apellido',
            'telefono',
            'correo',
            'fecha_nacimiento',
            'ciudad',
            'direccion',
            'nivel_educativo',
            'especialidad',
            'anos_experiencia',
            'activo',
            'fecha_vinculacion',
        ]
        # Widgets personalizados para mejorar la interfaz en el HTML
        widgets = {
            'documento_identidad': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el documento'
            }),
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el nombre'
            }),
            'apellido': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el apellido'
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '3001234567'
            }),
            'correo': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'correo@ejemplo.com'
            }),
            'fecha_nacimiento': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'ciudad': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ciudad de residencia'
            }),
            'direccion': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Dirección'
            }),
            'nivel_educativo': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Nivel Educativo'
            }),
            'especialidad': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Especialidad'
            }),
            'anos_experiencia': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Años de Experiencia'
            }),
            'activo': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Activo'
            }),
            'fecha_vinculacion': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
        }
        # Etiquetas personalizadas
        labels = {
            'documento_identidad': 'Documento de Identidad',
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'telefono': 'Teléfono',
            'correo': 'Correo Electrónico',
            'fecha_nacimiento': 'Fecha de Nacimiento',
            'ciudad': 'Ciudad',
            'direccion': 'Dirección',
            'nivel_educativo': 'Nivel Educativo',
            'especialidad': 'Especialidad',
            'anos_experiencia': 'Años de Experiencia',
            'activo': 'Activo',
            'fecha_vinculacion': 'Fecha de Vinculación'
        }

    # Validaciones personalizadas
    
    def clean_documento_identidad(self):
        """Validar que el documento contenga solo números"""
        documento = self.cleaned_data.get('documento_identidad')
        if not documento.isdigit():
            raise forms.ValidationError("El documento debe contener solo números.")
        return documento

    def clean_telefono(self):
        """Validar que el teléfono contenga solo números"""
        telefono = self.cleaned_data.get('telefono')
        if telefono and not telefono.isdigit():
            raise forms.ValidationError("El teléfono debe contener solo números.")
        if telefono and len(telefono) != 10:
            raise forms.ValidationError("El teléfono debe tener 10 dígitos.")
        return telefono