from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('galeria', views.galeria, name='galeria'),
    path('contacto', views.contacto, name='contacto'),
    path('nosotros', views.nosotros, name='nosotros'),
    # path('loginCliente', views.loginCliente, name='loginCliente'),
    # path('registroCliente', views.registroCliente, name='registroCliente'),
]
