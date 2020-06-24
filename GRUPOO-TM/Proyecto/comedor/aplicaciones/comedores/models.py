from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    # por ej: litros, kilos, unidades...
    tipo_cantidad = models.CharField(max_length=40)     
    cantidad = models.IntegerField()
    #fecha_creacion = models.DateTimeField(auto_now_add=True)
    #ultima_modificacion = models.DateTimeField(auto_now=True)
    
    
class Comedor(models.Model):
    nombre = models.CharField(max_length=30)
    ubicacion = models.CharField(max_length=50)
    descripcion = models.TextField()    
    productos_faltantes = models.ManyToManyField(Producto, related_name="producto", symmetrical=False)
    
    def obtener_demanda(self):
        return self.productos_faltantes.all()
        