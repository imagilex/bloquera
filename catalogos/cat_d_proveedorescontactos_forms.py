from django import forms
from .models import Cat_D_ProveedoresContactos

class frmCat_D_ProveedoresContactos(forms.ModelForm):

    class Meta:
        model = Cat_D_ProveedoresContactos
        fields = [
            'IDProveedor',
            'NombreContacto',
            'CargoContacto',
            'SucursalContacto',
            'DireccionContacto',
            'Email',
            'Telefono1',
            'Telefono2',
            'Telefono3',
            'Comentarios',
        ]
