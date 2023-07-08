from django.shortcuts import render
from django.shortcuts import redirect
from .forms import CuadroForm
from tienda.models import Cuadro
import urllib.request
import json
from django.contrib.auth.decorators import login_required, permission_required

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

#@login_required
def carro(request):
    cuadros = Cuadro.objects.all()
    context = {
        'cuadros': cuadros
    }
    return render(request, 'tienda/carro.html', context)    

def poke(request):
    if request.method == 'POST':
        pokemon = request.POST['pokemon'].lower()
        pokemon = pokemon.replace(' ', '%20')
        url_pokeapi = urllib.request.Request(
            f'https://pokeapi.co/api/v2/pokemon/{pokemon}/')
        url_pokeapi.add_header('User-Agent', 'charmander')

        source = urllib.request.urlopen(url_pokeapi).read()
        list_of_data = json.loads(source)
        # sprites = (list_of_data['sprites'])

        data = {
            "number": str(list_of_data['id']),
            "nombre": str(list_of_data['name']),
            "foto": str(list_of_data['sprites']['front_default']),
            'form': CuadroForm()
        }


        
    else:
        data = {}

    return render(request, 'tienda/poster_customer.html', data)    

@permission_required('tienda.add_cuadro')
def cuadrosAdd(request):
    context = {
        'form': CuadroForm()
    }
    if request.method == 'POST':
        form = CuadroForm(request.POST, files=request.FILES)
        if form.is_valid:
            form.save()
            context = {'mensaje': "Cuadro creado correctamente!"}

    return render(request, 'tienda/cuadrosAdd.html', context)

def posterAdd(request, nombre, foto, number):
    context = {
        'form': CuadroForm(),
        'nombre': nombre,
        'foto': foto,
        'number': number
    }
    if request.method == 'POST':
        form = CuadroForm(request.POST, files=request.FILES)
        if form.is_valid:
            form.save()
            context = {'mensaje': "Poster creado correctamente!"}

    return render(request, 'tienda/posterAdd.html', context)

@permission_required('tienda.change_cuadro')
def cuadrosEdit(request,id):
    cuadro = Cuadro.objects.get(id_cuadro = id)
    context = {
        'form': CuadroForm(instance=cuadro)
    }

    print({cuadro})
    if request.method == 'POST':
        form = CuadroForm(data=request.POST, files=request.FILES, instance=cuadro)
        if form.is_valid:
            form.save()
            context = {'mensaje': "Cuadro editado correctamente!"}

    return render(request, 'tienda/cuadrosEdit.html', context)

@permission_required('tienda.delete_cuadro')
def cuadrosDelete(request, id_cuadro):
    cuadro = Cuadro.objects.get(id_cuadro = id_cuadro)
    cuadro.delete()
    return redirect(to='galeria')
