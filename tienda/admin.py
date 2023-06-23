from django.contrib import admin
from .models import Cuadro, Cliente, Pedido, Carrito

# Register your models here.
admin.site.register(Cuadro)
admin.site.register(Cliente)
admin.site.register(Pedido)
admin.site.register(Carrito)