from django import forms
from .models import Cat_M_Cliente

class frmCat_M_Cliente(forms.ModelForm):

    class Meta:
        model = Cat_M_Cliente
        fields = [
            'IDCliente',
            'NombreCliente',
            'NombreVendedor',
            'Empresa',
            'Rfc',
            'DirFiscal',
            'Email',
            'Telefono1',
            'WhatsApp',
            'Telefono2',
        ]




