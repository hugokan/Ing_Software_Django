from django.shortcuts import render
from .models import Persona

# Create your views here.

def list_personas(request):
    persona = Personas.objects.all()
    return render(request, 'persona/persona.html', {'persona': personas})
