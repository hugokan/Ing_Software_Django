from django.db import models
from django.utils import timezone

# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.IntegerField()
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    titulo = models.CharField('titulo', blank=False, max_length=150)
    descripcion = models.TextField('Resumen', blank=True)
    nombre = models.ForeignKey(Persona, on_delete=models.CASCADE)
    apellido = models.ForeignKey(Persona, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class Compra(models.Model):
    nombre = models.ForeignKey(Persona, on_delete=models.CASCADE)
    telefono = models.ForeignKey(Persona, on_delete=models.CASCADE)
    titulo = models.ForeignKey(Producto, on_delete=models.CASCADE)
    descripcion = models.ForeignKey(Producto, on_delete=models.CASCADE)
    fecha = models.DateTimeField(default=timezone.now)
    hora = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo
