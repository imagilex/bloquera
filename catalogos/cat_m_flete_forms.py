from django import forms
from .models import Cat_M_Flete

class frmCat_M_Flete(forms.ModelForm):
    
    class Meta:
        model = Cat_M_Flete
        fields = [
            'IDFlete',
            'Nombre',
            'NombreProveedor',
            'CapacidadMinimaTarimas',
            'CapacidadMaximaTarimas',
            'Precio',
            'KilometrosMaxDistancia',
            'Comentarios',
        ]
