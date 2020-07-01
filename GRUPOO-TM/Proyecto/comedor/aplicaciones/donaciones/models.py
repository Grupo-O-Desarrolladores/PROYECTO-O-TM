from django.db import models
from aplicaciones.comedores.models import Comedor, Producto

class Donacion(models.Model):
    #cantidad = models.IntegerField()
    nombre_donante = models.CharField(max_length=30)
    contacto_donante = models.CharField(max_length=40)
    comedor_donacion = models.ForeignKey(Comedor, on_delete=models.CASCADE)
    producto_donacion = models.ForeignKey(Producto, on_delete=models.CASCADE)
    donacion_aceptada = models.BooleanField(default=False)
    def __str__(self):
        return 'Donacion para ' + self.comedor_donacion.nombre
