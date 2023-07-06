from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from .forms import crearUsuario

# Create your views here.
@login_required
def menu(request):
    #request.session["usuario"]="David"
    #usuario = request.session["usuario"]
    #context = {'usuario':usuario}
    return render(request, 'administrador/menu.html')

def salir(request):
    logout(request)
    return redirect("index")

#def posters(request):
    #traer lista de posters ingresados
    
def registro(request):
    data = {
        'form': crearUsuario()
    }
    if request.method == 'POST':
        formulario = crearUsuario(request.POST)
        if formulario.is_valid():
            formulario.save()
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect("index")

    return render(request, 'registration/registro.html', data)

