from django.shortcuts import render

# Create your views here.

def alumnos_list(request):
    return render(request,'crud/alumno_list.html', {})

def carreras_list(request):
    return render(request,'crud/carrera_list.html', {})
