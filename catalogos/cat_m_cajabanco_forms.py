from django import forms
from .models import Cat_M_CajaBanco

class frmCat_M_CajaBanco(forms.ModelForm):
    
    class Meta:
        model = Cat_M_CajaBanco
        fields = [
            'IDCajaBanco',
            'NombreCajaBanco',
            'Sucursal',
            'Direccion',
            'Num_CLABE',
            'Num_Cuenta',
            'Titular',
            'TipoCuenta',
            'NomBanco',
            'Ejecutivo',
            'Telefono1',
            'Telefono2',
        ]
