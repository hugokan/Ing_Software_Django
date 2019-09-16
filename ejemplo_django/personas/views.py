from django.shortcuts import render
from .models import Persona

# Create your views here.

def list_personas(request):
    persona = Persona.objects.all()
    return render(request, 'persona.html', {'persona': persona})


def list_productos(request):
    producto = Producto.objects.all()
    return render(request, 'producto.html', {'producto': persona})


def list_compras(request):
    compra = Compra.objects.all()
    return render(request, 'compra.html', {'compra': persona})
