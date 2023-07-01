from django.shortcuts import render

# Create your views here.
def menu(request):
    request.session["usuario"]="David"
    usuario = request.session["usuario"]
    context = {'usuario':usuario}
    return render(request, 'administrador/menu.html', context)

def home(request):
    context = {}
    return render(request, 'administrador/home.html', context)

#def posters(request):
    #traer lista de posters ingresados