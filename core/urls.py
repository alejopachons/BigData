from django.contrib import admin
from django.urls import path, include
from .views import GetNumbers, Suma, Resta, Potencia
from . import views

urlpatterns = [
    path('', GetNumbers.as_view(), name="home"),
    path('suma/', Suma.as_view(), name="suma"),
    path('resta/', Resta.as_view(), name="resta"),
    path('potencia/', Potencia.as_view(), name="potencia"),    
]
