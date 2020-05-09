from django import forms
from .models import Cat_M_MateriaPrima

class frmCat_M_MateriaPrima(forms.ModelForm):

    class Meta:
        model = Cat_M_MateriaPrima
        fields = [
            'IDProducto',
            'NombreProducto',
            'IDFoto',
            'UnidadMedida',
            'ExistenciaActual',
        ]
      