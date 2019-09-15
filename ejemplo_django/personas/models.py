from django.db import models

# Create your models here.

class Persona(models.Model):
    Nombre = models.CharField(max_length=100)
    Apellido = models.CharField(max_length=100)
    Telefono = models.IntegerField()
    Email = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Personas"
