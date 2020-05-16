from django import forms
from .models import Cat_M_Proveedores

class frmCat_M_Proveedores(forms.ModelForm):
    
    class Meta:
        model = Cat_M_Proveedores
        fields = [
            'IDProveedor',
            'NombreProveedor',
            'Empresa',
            'Rfc',
            'DirFiscal',
            'Telefono1',
            'Telefono2',
            'Telefono3',
            'Email',
        ]
