from django.contrib import admin
from aplicaciones.comedores.models import Producto, Comedor

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo_cantidad', 'cantidad')
    search_fields = ['nombre']
    pass
    
class ComedorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ubicacion')
    search_fields = ['nombre']
    pass
    
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Comedor, ComedorAdmin)