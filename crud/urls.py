from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.alumnos_list),
    path('saludo', views.saludo_bienvenida) 
]
