from django.db import models

class Aprendiz(models.Model):
    documento_identidad = models.CharField(max_length=100,unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100,null=True)
    correo = models.EmailField(max_length=100)
    fecha_nacimiento = models.DateField()
    ciudad = models.CharField(max_length=100,null=True)
    programa = models.CharField(max_length=100)
# Create your models here.

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.documento_identidad}"
    def get_full_name(self):
        return f"{self.nombre} {self.apellido}"
