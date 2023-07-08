from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('carro', views.carro, name='carro'),
    path('carro2', views.carro2, name='carro2'),
    path('galeria', views.galeria, name='galeria'),
    path('contacto', views.contacto, name='contacto'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('cuadrosAdd', views.cuadrosAdd, name='cuadrosAdd'),
    path('poster_customer', views.poke,  name='poster_customer'),
    path('cuadrosEdit/<str:id>', views.cuadrosEdit, name='cuadrosEdit'),
    path('cuadrosDelete/<str:id_cuadro>', views.cuadrosDelete,  name='cuadrosDelete'),
    path('posterAdd/<str:nombre>/<str:foto>/<str:number>', views.posterAdd,  name='posterAdd'),
]
