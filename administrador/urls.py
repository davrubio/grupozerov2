from django.urls import path
from . import views

urlpatterns = [
    path('salir/', views.salir, name='salir'),
    path('registro', views.registro, name='registro'),
]
