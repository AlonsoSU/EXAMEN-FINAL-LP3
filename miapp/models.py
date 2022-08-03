from django.db import models

# Create your models here.

class Articulo(models.Model):
    titulo = models.CharField(max_length=150)
    contenido = models.TextField()
    imagen = models.ImageField(default = 'null')
    publicado = models.BooleanField()
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

class Categoria(models.Model):
    nombre = models.CharField(max_length=110)
    descripcion = models.CharField(max_length=250)
    creado = models.DateField()

class Curso(models.Model):
    codigo = models.CharField(max_length=110)
    nombre = models.TextField(max_length=250)
    precio_compra = models.FloatField()
    precio_venta = models.FloatField()
    Fecha_compra = models.DateField()
    Fecha_registro = models.DateField()
    estado = models.BooleanField()