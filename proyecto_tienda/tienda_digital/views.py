from django.shortcuts import redirect, render
from tienda_digital.models import Producto
from tienda_digital.forms import ProductoForm
from django.forms import modelform_factory
from django.core.paginator import Paginator


ProductoForm = modelform_factory(Producto, exclude=[])



def mostrar_productos(request):
    productos = Producto.objects.all()

    items_por_pagina = request.GET.get('paginador', 12)

    page_number = request.GET.get('page')

    paginador = Paginator(productos, items_por_pagina)
    page_obj = paginador.get_page(page_number)

    return render(request, 'mostrar_productos.html', {'page_obj': page_obj,})



def agregar_producto(request):
    if request.method == 'POST':
        producto_form = ProductoForm(request.POST, request.FILES)

        if producto_form.is_valid():
            producto_form.save()
            return redirect('mostrar_productos')

    else:
        producto_form = ProductoForm()
        
    data = {'producto_form':producto_form}
    return render(request, "agregar_producto.html", data)


def actualizar_producto():
    pass

def eliminar_producto():
    pass