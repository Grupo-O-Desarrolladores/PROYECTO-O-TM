from django.contrib import admin
from aplicaciones.donaciones.models import Donacion

class DonacionAdmin(admin.ModelAdmin):
    list_display = ('nombre_donante', 'contacto_donante', 'donacion_aceptada')
    search_fields = ['nombre_donante']    
    pass
    
admin.site.register(Donacion, DonacionAdmin)