from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    # por ej: litros, kilos, unidades...
    tipo_cantidad = models.CharField(max_length=40)     
    cantidad = models.IntegerField()
    # Aun no estoy seguro porque no logro conectar esta parte. Me salen errores en la migracion.
    # Pendiente...
    #fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)
    #ultima_modificacion = models.DateTimeField(auto_now=True)
    def __str__(self):
        return 'Producto ' + self.nombre
    
    
class Comedor(models.Model):
    nombre = models.CharField(max_length=30)
    ubicacion = models.CharField(max_length=50)
    descripcion = models.TextField(null=True)    
    productos_faltantes = models.ManyToManyField(Producto, related_name="producto", symmetrical=False)
    
    def obtener_demanda(self):
        return self.productos_faltantes.all()
    def __str__(self):
        return 'Comedor ' + self.nombre