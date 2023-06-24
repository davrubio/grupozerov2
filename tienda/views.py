from django.shortcuts import render

from tienda.models import Cuadro, Cliente, Pedido, Carrito

# Create your views here.
# def index(request):
#     context = {}
#     return render(request, 'tienda/index.html')
    

def index(request):
    cuadros = Cuadro.objects.all()
    context = {
        'cuadros': cuadros
    }
    return render(request, 'tienda/index.html', context)


def contacto(request):
    context = {}
    return render(request, 'tienda/contacto.html')
    
def nosotros(request):
    context = {}
    return render(request, 'tienda/nosotros.html')

def galeria(request):
    cuadros = Cuadro.objects.all()
    context = {
        'cuadros': cuadros
    }
    return render(request, 'tienda/galeria.html', context)