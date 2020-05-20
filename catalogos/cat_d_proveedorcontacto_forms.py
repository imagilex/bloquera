from django import forms
from .models import Cat_D_ProveedorContacto

class frmCat_D_ProveedorContacto(forms.ModelForm):

    class Meta:
        model = Cat_D_ProveedorContacto
        fields = [
            'IDProveedor',
            'NombreContacto',
            'CargoContacto',
            'SucursalContacto',
            'DireccionContacto',
            'Email',
            'Telefono1',
            'WhatsApp',
            'Telefono2',
            'Comentarios',
        ]
