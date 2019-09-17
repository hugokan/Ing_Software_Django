from django.shortcuts import render

from .models import Persona, Compra, Producto

# Create your views here.
def compra_list(request):
    compra = Compra.objects.all()
    return render(request, 'ejercicio/compra_list.html', {'compra':compra})


def persona_list(request):
    persona = Persona.objects.all()
    return render(request, 'ejercicio/persona_list.html', {'persona':persona})


def producto_list(request):
    producto = Producto.objects.all()
    return render(request, 'ejercicio/producto_list.html', {'producto':producto})


def index(request):
    return render(request, 'ejercicio/index.html', {})
