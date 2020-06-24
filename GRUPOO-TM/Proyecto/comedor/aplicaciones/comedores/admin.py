from django.contrib import admin
from aplicaciones.comedores.models import Producto, Comedor

class ProductoAdmin(admin.ModelAdmin):
    pass
    
class ComedorAdmin(admin.ModelAdmin):
    pass
    
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Comedor, ComedorAdmin)