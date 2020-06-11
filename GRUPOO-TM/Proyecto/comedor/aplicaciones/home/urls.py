
from django.urls import path
from . import views

app_name = "home_app"

urlpatterns = [
    path('', views.InicioView.as_view(), name="inicio"),
    path('about', views.AcercaDeView.as_view(), name="about"),
]
