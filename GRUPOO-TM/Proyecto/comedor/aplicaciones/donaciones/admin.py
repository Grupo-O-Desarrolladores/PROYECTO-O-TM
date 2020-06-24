from django.contrib import admin
from aplicaciones.donaciones.models import Donacion

class DonacionAdmin(admin.ModelAdmin):
    pass
    
admin.site.register(Donacion, DonacionAdmin)