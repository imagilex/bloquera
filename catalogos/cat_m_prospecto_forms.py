from django import forms
from .models import Cat_M_Prospecto

class frmCat_M_Prospecto(forms.ModelForm):

    class Meta:
        model = Cat_M_Prospecto
        fields = [
            'IDProspecto',
            'Nombre',
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
            'Telefono2',
            'Telefono3',
            'Direccion',
            'Estatus',
            'Comentarios',
        ]
        
