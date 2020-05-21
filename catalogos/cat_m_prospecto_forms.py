from django import forms
from .models import Cat_M_Prospecto

class frmCat_M_Prospecto(forms.ModelForm):

    class Meta:
        model = Cat_M_Prospecto
        fields = [
            'IDProspecto',
            'NombreProspecto',
            'TipoCaptacion',
            'UsoMaterial',
            'Constructora',
            'CasaMateriales',
            'ProductosInteres',
            'FechaRegistro',
            'NombreVendedor',
            'Puesto',
            'Email',
            'Telefono1',
            'WhatsApp',
            'Telefono2',
            'Direccion',
            'Estatus',
            'Comentarios',
        ]
        
