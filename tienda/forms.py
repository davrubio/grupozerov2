from dataclasses import fields
from django import forms
from django.forms import ModelForm
from .models import Cliente

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['rut_cliente',
                  'nombre',
                  'ap_paterno',
                  'ap_materno',
                  'fono',
                  'correo',
                  'direccion',
                  'password']