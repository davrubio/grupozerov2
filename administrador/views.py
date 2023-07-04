from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

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