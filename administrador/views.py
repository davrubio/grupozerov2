from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from .forms import crearUsuario
from django.contrib import messages

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
            user = authenticate(username=formulario.cleaned_data["username"],
                                password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect("login")
        data["form"] = formulario            
    return render(request, 'registration/registro.html', data)

