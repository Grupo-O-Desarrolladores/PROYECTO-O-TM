"""comedor URL Configuration
Archivo de urls general. Administra todos los urls de todas las aplicaciones.
"""
from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    re_path(r'^', include('aplicaciones.home.urls')),
    re_path(r'^', include('aplicaciones.comedores.urls')),
    re_path(r'^', include('aplicaciones.donaciones.urls')),
    path('admin/', admin.site.urls),
]
