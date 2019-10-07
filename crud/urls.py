from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.alumnos_list),
  
    
]

urlpatterns = [
    path('', views.carreras_list),
]