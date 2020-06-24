from django.shortcuts import render
from aplicaciones.comedores.models import Producto, Comedor

def comedor_index(request):
    comedores = Comedor.objects.all()
    context = {
        'comedores': comedores,
    }
    
    return render(request, 'comedores/comedor_index.html', context)
    
    
def comedor_detalle(request, nombre):
    este_comedor = Comedor.objects.get(nombre=nombre)
    productos = Comedor.obtener_demanda(este_comedor)
    context = {
        'comedor': este_comedor,
        'nombre': nombre,
        'productos': productos,
    }
    
    return render(request, 'comedores/comedor_detalle.html', context)