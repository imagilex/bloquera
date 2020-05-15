from django import forms
from .models import Tbl_M_MovtosInventario

class frmTbl_M_MovtosInventario(forms.ModelForm):

    class Meta:
        model = Tbl_M_MovtosInventario
        fields = [
            'IDPeriodo',
            'IDMovimiento',
            'IDProducto',
            'IDPlanProducción',
            'IDVentaIDMovimiento',
            'IDCompra',
            'IDTipoMovimiento',
            'FechaMovto',
            'Cantidad',
            'Observaciones',
            'IdEmpleado'
        ]