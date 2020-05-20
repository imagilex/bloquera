from django import forms
from .models import Cat_M_Inventario

class frmCat_M_Inventario(forms.ModelForm):
    
    class Meta:
        model = Cat_M_Inventario
        fields = [
            'IDProducto',
            'IDTipoProducto',
            'NombreProducto',
            'IDFoto',
            'FechaAlta',
            'UnidadMedida',
            'ExistenciaActual',
            'ExistenciaMaxima',
            'ExistenciaMinima',
            'Observaciones',
            'DiasPromedioResurtimiento',
            'Produccionmaxdia',
            'CostoUnitarioultimaProducción',
            'Preciocostoultimacompra',
            'Preciovtaultimaproduccion',
            'Preciovtaunitarioultimaproduccion',
            'Estatus',

        ]