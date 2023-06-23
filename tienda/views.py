from django.shortcuts import render

from tienda.models import Cuadro, Cliente, Pedido, Carrito

# Create your views here.
def index(request):
    context = {}
    return render(request, 'tienda/index.html')

def galeria(request):
    cuadros = Cuadro.objects.all()
    context = {
        'cuadros': cuadros
    }
    return render(request, 'tienda/galeria.html', context)