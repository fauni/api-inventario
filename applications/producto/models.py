from django.db import models
from .choices import estados, tiposmovimiento

from django.utils.timezone import now

# Create your models here.
class Almacen(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    lugar = models.CharField(max_length=64)
    direccion = models.CharField(max_length=255)
    estado = models.CharField(max_length=1, choices=estados,default='A')

class Categoria(models.Model):
    descripcion = models.CharField(max_length=100)
    estado = models.CharField(max_length=1, choices=estados, default='A')

class Grupo(models.Model):
    descripcion = models.CharField(max_length=100)
    estado = models.CharField(max_length=1, choices=estados, default='A')

class Proveedor(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    nit = models.CharField(max_length=20)
    contacto = models.CharField(max_length=250)
    celular = models.CharField(max_length=8)
    estado = models.CharField(max_length=1, choices=estados, default='A')

class Producto(models.Model):
    codigo = models.CharField(max_length=50)
    codigo_barras = models.CharField(max_length=255)
    nombre = models.CharField(max_length=200)
    detalle = models.CharField(max_length=200)
    categoria = models.ForeignKey(Categoria, null=True, blank=True, on_delete=models.CASCADE)
    grupo = models.ForeignKey(Grupo, null=True, blank=True,on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedor, null=True, blank=True, on_delete=models.CASCADE)
    imagen = models.CharField(max_length=150)
    usa_inventarios = models.BooleanField(default=True)
    usa_lotes = models.BooleanField(default=False)
    stock = models.IntegerField()
    stock_minimo = models.IntegerField()
    precio_compra = models.DecimalField(max_digits=7, decimal_places=2)
    precio_venta = models.DecimalField(max_digits=7, decimal_places=2)
    estado = models.CharField(max_length=1, choices=estados, default='A')

class ProductoLote(models.Model):
    producto = models.ForeignKey(Producto, null=True, blank=True, on_delete=models.CASCADE)
    lote = models.CharField(max_length=30)
    fecha_recepcion = models.DateTimeField(null=True)
    fecha_vencimiento = models.DateTimeField(null=True)
    fecha_limite_venta = models.DateTimeField(null=True)

class ProductoStock(models.Model):
    fecha = models.DateTimeField(null=True)
    producto = models.ForeignKey(Producto, null=True, blank=True, on_delete=models.CASCADE)
    almacen = models.ForeignKey(Almacen, null=True, blank=True, on_delete=models.CASCADE)
    valor = models.BigIntegerField()
    
class MovimientoStock(models.Model):
    fecha = models.DateTimeField()
    producto = models.ForeignKey(Producto, null=True, blank=True, on_delete=models.CASCADE)
    lote = models.CharField(max_length=30,null=True, blank=True)
    almacen = models.ForeignKey(Almacen, null=True, blank=True, on_delete=models.CASCADE)
    valor = models.BigIntegerField()
    precio = models.DecimalField(max_digits=7, decimal_places=2)
    tipo_movimiento = models.CharField(max_length=1, choices=tiposmovimiento, null=True)
