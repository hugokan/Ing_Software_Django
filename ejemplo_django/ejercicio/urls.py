from django.urls import path
from . import views

urlpatterns = [
    path('compra/', views.compra_list, name='compra_list'),
    path('persona/', views.persona_list, name='persona_list'),
    path('producto/', views.producto_list, name='producto_list'),
    path('', views.index, name='index'),
]
