from django import forms
from .models import Cat_D_Prospecto

class frmCat_D_Prospecto(forms.ModelForm):

    class Meta:
        model = Cat_D_Prospecto
        fields = [
            'Prospecto',
            'FechaNota',
            'ProximoSeguimiento',
            'Seguimiento',
        ]
        