from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.compra, name="compra"),
    path('persona/', views.persona, name="persona"),
    path('producto/', views.producto, name="producto"),
]
