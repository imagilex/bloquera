from django import forms
from .models import Tbl_M_MovtosInventario

class frmTbl_M_MovtosInventario(forms.ModelForm):

    class Meta:
        model = Tbl_M_MovtosInventario
        fields = [
            'IDMovimiento',
            'IDPeriodo',
            'IDPlanProducción',
            'IDVenta',
            'IDCompra',
            'IDTipoMovimiento',
            'NombreProducto',
            'FechaMovto',
            'Cantidad',
            'Observaciones',
            'IdEmpleado'
        ]