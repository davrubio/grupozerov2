from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

# class formularioLogin(AuthenticationForm):
    
    
#     class Meta:
#         model = User
#         fields = ['username',
#                   'password']
    
#     username = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Username', 'name':"username"}))
#     password = forms.CharField(label='',widget=forms.PasswordInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Contraseña', 'type':"password"}))

class crearUsuario(UserCreationForm):
    
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Username'}))
    first_name = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Nombre'}))
    last_name = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Apellido'}))
    email = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Email'}))
    password1 = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Contraseña', 'type':"password"}))
    password2 = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Repetir contraseña', 'type':"password"}))
    
    class Meta:
        model = User
        fields = ['username',
                  'first_name',
                  'last_name',
                  'email',
                  'password1',
                  'password2']
        
    
    