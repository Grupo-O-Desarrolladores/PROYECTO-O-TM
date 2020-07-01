from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    # por ej: litros, kilos, unidades...
    tipo_cantidad = models.CharField(max_length=40)
    # cantidad requerida del mismo
    cantidad = models.IntegerField()
    # esta función me ayuda para visuarlizar en el administrador
    def __str__(self):
        return 'Producto ' + self.nombre
    
    
class Comedor(models.Model):
    nombre = models.CharField(max_length=30)
    ubicacion = models.CharField(max_length=50)
    descripcion = models.TextField(null=True)    
    # productos de la clase Producto que se requieren para este comedor
    productos_faltantes = models.ManyToManyField(Producto, related_name="producto", symmetrical=False)
    
    def obtener_demanda(self):
        return self.productos_faltantes.all()
    # esta función me ayuda para visuarlizar en el administrador
    def __str__(self):
        return 'Comedor ' + self.nombre
