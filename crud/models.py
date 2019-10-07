from django.db import models
from django.utils import timezone
# Create your models here.

class Carrera(models.Model):
    nombre=models.CharField(max_length=40)
    semestre=models.IntegerField()
    mensualidad=models.IntegerField()
    
    def __str__(self):
        return self.nombre
    
class Alumno (models.Model):
    Carrera=models.ForeignKey(Carrera, null=True, blank=True, on_delete=models.CASCADE)
    rut=models.CharField(max_length=15)
    nombre=models.CharField(max_length=50)
    apellidoPaterno=models.CharField(max_length=50)
    apellidoMaterno=models.CharField(max_length=50)
    edad=models.IntegerField()
    telefono=models.CharField(max_length=20)
    domicilio=models.TextField()
    fecha_registro=models.DateTimeField(auto_now=True)
    fecha_nacimiento=models.DateField()

    def __str__(self):
        return self.nombre
