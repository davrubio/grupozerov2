from django.db import models

# Create your models here.

class Cuadro(models.Model):
    id_cuadro = models.AutoField(db_column = 'idCuadro', primary_key=True)
    titulo = models.CharField(max_length=40, null = False)
    artista = models.CharField(max_length=80, null = False)
    descripcion = models.CharField(max_length=400, null = False)
    precio = models.IntegerField(null = False)
    anno_creacion = models.DateField(blank=False, null = False)
    imagen = models.ImageField(upload_to="cuadros", null=False)
    
    def __str__(self):
        return str(self.titulo)
    
class Pedido(models.Model):
    id_pedido = models.AutoField(db_column = 'idPedido', primary_key=True)
    estado = models.IntegerField()
    total = models.IntegerField()
    
    def __str__(self):
        return str(self.estado)
    
class Carrito(models.Model):
    id_compra = models.AutoField(db_column='idCompra', primary_key=True)
    cantidad = models.IntegerField()
    id_cuadro = models.ForeignKey('Cuadro', on_delete=models.CASCADE, db_column='id_cuadro')
    id_pedido = models.ForeignKey('Pedido', on_delete=models.CASCADE, db_column='id_pedido')
    