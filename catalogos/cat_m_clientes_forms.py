from django import forms
from .models import Cat_M_Clientes

class frmCat_M_Clientes(forms.ModelForm):

    class Meta:
        model = Cat_M_Clientes
        fields = [
            'IDCliente',
            'NombreCliente',
            'NombreProveedor',
            'Empresa',
            'Rfc',
            'DirFiscal',
            'Email',
            'Telefono1',
            'Telefono2',
            'Telefono3',
        ]




