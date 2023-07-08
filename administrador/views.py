from typing import Any
from django import http
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from .forms import crearUsuario
from django.views.generic.edit import FormView


# Create your views here.
# @login_required
# def menu(request):
#     #request.session["usuario"]="David"
#     #usuario = request.session["usuario"]
#     #context = {'usuario':usuario}
#     return render(request, 'administrador/menu.html')

# class Login(FormView):
#     template_name = 'login.html'
#     form_class = 'FormularioLogin'
#     success_url = reverse_lazy('index')
    
#     @method_decorator(csrf_protect)
#     @method_decorator(never_cache)
#     def dispatch(self, request, *args, **kwargs):
#         if request.user.is_authenticated:
#             return HttpResponseRedirect(self.get_success_url)
#         else:
#             return super(Login, self).dispatch(request, *args, **kwargs)
        
#     def form_valid(self, form):
#         login(self.request, form.get_)
#         return super().form_valid(form)

# def login(request):
#     data = {
#         'form': formularioLogin()
#     }
#     if request.method == 'POST':
#         formulario = formularioLogin(request.POST)
#         if formulario.is_valid():
#             return redirect("index")    
        

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