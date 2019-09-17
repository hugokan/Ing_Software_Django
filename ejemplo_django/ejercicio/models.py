from django.db import models
from django.utils import timezone


class Persona(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    apellido = models.CharField(max_length=100, verbose_name="Apellido")
    telefono = models.CharField(max_length=50, verbose_name="Telefono")
    email = models.CharField(max_length=80, verbose_name="Email")

    class Meta:
        verbose_name = "cliente"
        verbose_name_plural = "clientes"

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título")
    marca = models.CharField(max_length=100, verbose_name="Marca")
    descripcion = models.TextField()
    nombre = models.ForeignKey('persona', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "producto"
        verbose_name_plural = "productos"

    def __str__(self):
        return self.titulo


class Compra(models.Model):
    precio = models.CharField(max_length=50)
    titulo = models.ForeignKey('producto', on_delete=models.CASCADE)
    nombre = models.ForeignKey('persona', on_delete=models.CASCADE)
    fecha_compra = models.DateTimeField(
            default=timezone.now)
    fecha_envio = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.fecha_envio = timezone.now()
        self.save()

    def __str__(self):
        return self.precio
