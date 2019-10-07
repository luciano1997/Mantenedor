from .models import Carrera, Alumno
from mantenedor.app.froms import CarreraForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# Create your views here.


def alumnos_list(request):
    return render(request, 'crud/alumno_list.html', {})


def saludo_bienvenida(request):
    return render(request, 'crud/saludo.html', {})

# ---- codigo para crear el add carrera el addCarrera para agregar un registro ---


def inscripcion_carrera(request):
    if request.method == "POST":
        form =
