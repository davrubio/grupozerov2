from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('carro', views.carro, name='carro'),
    path('galeria', views.galeria, name='galeria'),
    path('contacto', views.contacto, name='contacto'),
    path('nosotros', views.nosotros, name='nosotros'),
<<<<<<< HEAD
    # path('loginCliente', views.loginCliente, name='loginCliente'),
    # path('registroCliente', views.registroCliente, name='registroCliente'),
=======
    path('cuadrosAdd', views.cuadrosAdd, name='cuadrosAdd'),
    path('poster_customer', views.poke,  name='poster_customer'),
    path('cuadrosEdit/<str:id>', views.cuadrosEdit, name='cuadrosEdit'),
    path('cuadrosDelete/<str:id_cuadro>', views.cuadrosDelete,  name='cuadrosDelete'),
    path('posterAdd/<str:nombre>/<str:foto>/<str:number>', views.posterAdd,  name='posterAdd'),
>>>>>>> 24099a67da10e52c27a5666efd5e7aed157a1f4a
]
