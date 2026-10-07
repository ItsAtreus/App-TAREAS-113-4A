from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Producto

def inicio(request):
    # Consultamos todos los componentes en el inventario
    productos = Producto.objects.all()
    return render(request, 'tareasapp/inicio.html', {
        'productos': productos
    }) 

def crear_producto(request):
    error = None
    if request.method == 'POST':
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        precio = int(request.POST['precio'])
        stock = int(request.POST['stock'])
        categoria = request.POST['categoria']

        # Validaciones para precios y stock
        if precio <= 0:
            error = "El precio del componente debe ser mayor a cero."
        elif stock < 0:
            error = "El stock no puede ser negativo."
        else:
            Producto.objects.create(
                nombre=nombre,
                descripcion=descripcion,
                precio=precio,
                stock=stock,
                categoria=categoria
            )
            return redirect('inicio')
            
    return render(request, 'tareasapp/crear.html', {'error': error})

def detalle_producto(request, id):
    producto = Producto.objects.get(id=id)
    return render(request, 'tareasapp/detalle.html', {
        'producto': producto
    })

def editar_producto(request, id):
    producto = Producto.objects.get(id=id)
    error = None

    if request.method == 'POST':
        precio_nuevo = int(request.POST['precio'])
        stock_nuevo = int(request.POST['stock'])

        
        if precio_nuevo <= 0:
            error = "El precio del componente debe ser mayor a cero."
        elif stock_nuevo < 0:
            error = "El stock no puede ser negativo."
        else:
            producto.nombre = request.POST['nombre']
            producto.descripcion = request.POST['descripcion']
            producto.precio = precio_nuevo
            producto.stock = stock_nuevo
            producto.categoria = request.POST['categoria']
            
            producto.save()
            return redirect('inicio')
    
    return render(request, 'tareasapp/editar.html', {
        'producto': producto,
        'error': error
    })

def eliminar_producto(request, id):
    producto = Producto.objects.get(id=id)

    if request.method == 'POST':
        producto.delete()
        return redirect('inicio')
    
    return render(request, 'tareasapp/eliminar.html', {
        'producto': producto
    })