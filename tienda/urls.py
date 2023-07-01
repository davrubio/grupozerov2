from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('galeria', views.galeria, name='galeria'),
    path('contacto', views.contacto, name='contacto'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('cuadrosAdd', views.cuadrosAdd, name='cuadrosAdd'),
    path('poster_customer', views.poke, name='poster_customer'),
]
