from django.shortcuts import render, redirect
from aplicaciones.donaciones.models import Donacion
from aplicaciones.comedores.models import Comedor, Producto
from aplicaciones.donaciones.forms import FormaDonacion

# Pagina indice de donaciones, selecciono un comedor
def donaciones_index(request):
    comedores = Comedor.objects.all()
    context = {
        'comedores': comedores,
    }
    
    return render(request, 'donaciones/donaciones_index.html', context)
    
# Pagina donde selecciono que donar
def donaciones_seleccion(request, nombre):
    este_comedor = Comedor.objects.get(nombre=nombre)
    productos = Comedor.obtener_demanda(este_comedor)
    context = {
        'nombre': nombre,
        'productos': productos,
    }
    
    return render(request, 'donaciones/donaciones_seleccion.html', context)
# Pagina donde dono
def donaciones_donacion(request, nombre_producto, nombre):
    este_comedor = Comedor.objects.get(nombre=nombre)
    este_producto = Producto.objects.get(nombre=nombre_producto)
    forma = FormaDonacion()
    if request.method == 'POST':
        forma = FormaDonacion(request.POST)
        if forma.is_valid():
            donacion = Donacion(
                nombre_donante=forma.cleaned_data["donante"],
                contacto_donante=forma.cleaned_data["contacto"],
                comedor_donacion=este_comedor,
                producto_donacion=este_producto
            )
            donacion.save()
            return redirect ('donaciones_app:donaciones_index')
            
    context = {
        'nombre': este_comedor.nombre,
        'producto': este_producto,
        'forma': forma,
    }
    
    return render(request, 'donaciones/donaciones_donacion.html', context)