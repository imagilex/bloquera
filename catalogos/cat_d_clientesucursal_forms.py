from django import forms
from .models import Cat_D_ClienteSucursal

class frmCat_D_ClienteSucursal(forms.ModelForm):

    class Meta:
        model = Cat_D_ClienteSucursal
        fields = [
            'IDCliente',
            'NombreContacto',
            'Cargo',
            'Sucursal',
            'Direccion',
            'Email',
            'Telefono1',
            'WhatsApp',
            'Telefono2',
            'Comentarios',
        ]
