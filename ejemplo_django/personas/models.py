from django.db import models


# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    apellido = models.CharField(max_length=100, verbose_name="Apellido")
    telefono = models.CharField(max_length=100, verbose_name="Telefono")
    email = models.CharField(max_length=100, verbose_name="Email")

    class Meta:
        verbose_name = "persona"
        verbose_name_plural = "personas"
        ordering = ['-created']

    def __str__(self):
        return self.nombre
