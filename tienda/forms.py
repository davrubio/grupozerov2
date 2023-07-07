from dataclasses import fields
from django import forms
from django.forms import ModelForm
from .models import Cuadro

class CuadroForm(ModelForm):
    class Meta:
        model=Cuadro
        fields = ['id_cuadro',
        'titulo',
        'artista',
        'descripcion',
        'precio',
        'anno_creacion',
        'imagen',]
        
        print(f'{fields}')

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Ingrese un titulo', 'id':'titulo'}),
            'artista': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Ingrese nombre del artista', 'id':'artista'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Ingrese una breve descripción', 'id':'descripcion'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'Ingrese precio', 'id':'precio'}),
            'anno_creacion': forms.SelectDateWidget(years=range(1900,2022), attrs={'placeholder':'Ingrese año de la obra', 'id':'anno_creacion'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control','id':'imagen'})
        }