from django import forms
from tienda_digital.models import Producto


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'stock', 'categoria', 'imagen']
        labels = {
            'nombre': 'Nombre del Producto',
            'descripcion': 'Descripción',
        }