from django import forms
from .models import Cat_D_ClientesSucursales

class frmCat_D_ClientesSucursales(forms.ModelForm):

    class Meta:
        model = Cat_D_ClientesSucursales
        fields = [
            'IDCliente',
            'NombreContacto',
            'Cargo',
            'Sucursal',
            'Direccion',
            'Email',
            'Telefono1',
            'Telefono2',
            'Telefono3',
            'Comentarios',
        ]
