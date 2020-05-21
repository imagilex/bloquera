from django import forms
from .models import Cat_M_Vendedor

class frmCat_M_Vendedor(forms.ModelForm):

    class Meta:
        model = Cat_M_Vendedor
        fields = [
            'IDVendedor',
            'NombreVendedor',
            'Direccion',
            'Rfc',
            'Email',
            'Telefono1',
            'WhatsApp',
            'Telefono2',
            'Comentarios',
        ]
        
