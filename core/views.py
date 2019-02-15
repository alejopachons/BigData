from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from .forms import NumbersForm


# Create your views here.

class GetNumbers(FormView):
    template_name = 'core/home.html'
    form_class = NumbersForm

class Suma(TemplateView):
    template_name = 'core/suma.html'

class Resta(TemplateView):
    template_name = 'core/resta.html'

class Potencia(TemplateView):
    template_name = 'core/potencia.html'
