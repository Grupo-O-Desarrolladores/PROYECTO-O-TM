from django.shortcuts import render

# Create your views here.

from django.views.generic import (
    TemplateView,
)

class InicioView(TemplateView):
    template_name = "home/inicio.html"


class AcercaDeView(TemplateView):
    template_name = "home/about.html"