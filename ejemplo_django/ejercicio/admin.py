from django.contrib import admin
from .models import Persona
from .models import Producto
from .models import Compra

admin.site.register(Persona)
admin.site.register(Producto)
admin.site.register(Compra)
