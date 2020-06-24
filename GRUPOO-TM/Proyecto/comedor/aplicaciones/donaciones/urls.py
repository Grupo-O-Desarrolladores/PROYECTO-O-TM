from django.urls import path
from . import views

app_name = 'donaciones_app'

urlpatterns = [
    path('donaciones/', views.donaciones_index, name="donaciones_index"),
    path('donaciones/<nombre>/', views.donaciones_seleccion, name="donaciones_seleccion"),
    path('donaciones/<nombre>/<nombre_producto>/', views.donaciones_donacion, name="donaciones_donacion"),
]
