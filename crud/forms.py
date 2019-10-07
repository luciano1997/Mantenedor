from django import forms
from .models import Carrera, Alumno


class CarreraForm(forms.ModelForm):
    class Meta:
        model= Carrera
        fields= ['nombre', 'semestre', 'mensualidad']


#class ALumnoForm(forms.ModelForm):
#    class Meta:
#        model=Alumno
#        fields=['carrera','rut','nombre','apellido']        
