from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Cuadro, Cliente, Pedido, Carrito
from .forms import ClienteForm

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

def loginCliente(request):
    return render(request, 'tienda/registrationCliente/loginCliente.html')

def registroCliente(request):
    context = {
        'form': ClienteForm()
    }
    if request.method == 'POST':
        formulario = ClienteForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            context = {'mensaje': "Se ha registrado correctamente!"}
        else:
            context = {'mensaje': "Error en el ingreso de datos"}
    return render(request, 'tienda/registrationCliente/registroCliente.html', context)