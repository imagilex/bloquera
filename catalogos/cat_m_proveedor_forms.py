from django import forms
from .models import Cat_M_Proveedor

class frmCat_M_Proveedor(forms.ModelForm):
    
    class Meta:
        model = Cat_M_Proveedor
        fields = [
            'IDProveedor',
            'NombreProveedor',
            'Empresa',
            'Rfc',
            'DirFiscal',
            'Telefono1',
            'WhatsApp',
            'Telefono3',
            'Email',
        ]
