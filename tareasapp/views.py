from django.shortcuts import get_object_or_404, redirect, render

from .forms import ProductoForm
from .models import Producto


def inicio(request):
    productos = Producto.objects.all()
    return render(request, 'tareasapp/inicio.html', {'productos': productos})


def crear_producto(request):
    form = ProductoForm(request.POST if request.method == 'POST' else None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('inicio')
    return render(request, 'tareasapp/formulario.html', {
        'form': form,
        'titulo': 'Crear producto',
        'accion': 'Guardar producto',
    })


def detalle_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    return render(request, 'tareasapp/detalle.html', {'producto': producto})


def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    form = ProductoForm(
        request.POST if request.method == 'POST' else None,
        instance=producto,
    )
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('inicio')
    return render(request, 'tareasapp/formulario.html', {
        'form': form,
        'titulo': 'Editar producto',
        'accion': 'Guardar cambios',
    })


def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        producto.delete()
        return redirect('inicio')
    return render(request, 'tareasapp/eliminar.html', {'producto': producto})
