from django.db import models
from aplicaciones.comedores.models import Comedor

class Donacion(models.Model):
    #cantidad = models.IntegerField()
    nombre_donante = models.CharField(max_length=30)
    contacto_donante = models.CharField(max_length=40)
    comedor_donacion = models.ForeignKey(Comedor, on_delete=models.CASCADE)
    donacion_aceptada = False

