from django.urls import path
from . import views

urlpatterns = [
    path('comedores/', views.comedor_index, name="comedor_index"),
    path('comedores/<nombre>/', views.comedor_detalle, name="comedor_detalle"),
]
