from django.urls import path

from . import views

urlpatterns = [
    path('', views.personas, name="persona"),
]
