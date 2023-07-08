from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from .forms import crearUsuario

        

def salir(request):
    logout(request)
    return redirect("index")

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
            data = {'mensaje': "Se ha registrado correctamente"}
            # return redirect("login")
        data["form"] = formulario            
    return render(request, 'registration/registro.html', data)