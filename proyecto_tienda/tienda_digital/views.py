from django.shortcuts import redirect, render
from tienda_digital.models import Producto
from tienda_digital.forms import ProductoForm
from django.forms import modelform_factory


ProductoForm = modelform_factory(Producto, exclude=[])

def mostrar_productos(request):

    productos = Producto.objects.all()
    info_prod = {'productos': productos}

    return render(request, 'mostrar_productos.html', info_prod )


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