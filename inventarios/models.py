from django.db import models
from django.utils import timezone

from inventarios.models import Cat_M_Inventario

ESTATUS_PERIODO_TYPE = {
    '052020': '052020',
    '062020': '062020',
    '072020': '072020',
    '082020': '082020',
    '092020': '092020',
    '102020': '102020',
    '112020': '112020',
    '122020': '122020',
}

ESTATUS_PERIODO_TYPE_Tuples = (
        (ESTATUS_PERIODO_TYPE['052020'], '052020'),
        (ESTATUS_PERIODO_TYPE['062020'], '062020'),
        (ESTATUS_PERIODO_TYPE['072020'], '072020'),
        (ESTATUS_PERIODO_TYPE['072020'], '072020'),
        (ESTATUS_PERIODO_TYPE['072020'], '072020'),
        (ESTATUS_PERIODO_TYPE['072020'], '072020'),
        (ESTATUS_PERIODO_TYPE['072020'], '072020'),
        (ESTATUS_PERIODO_TYPE['072020'], '072020'),
    )

FORMULA_TYPE = {
    'CANCELADO': 'CANCELADO',
    'ENPROCESO': 'EN PROCESO',
    'VIGENTE': 'VIGENTE',
}

FORMULA_TYPE_Tuples = (
        (FORMULA_TYPE['CANCELADO'], 'CANCELADO'),
        (FORMULA_TYPE['ENPROCESO'], 'EN PROCESO'),
        (FORMULA_TYPE['VIGENTE'], 'VIGENTE'),
    )


# Create your models here.
class Tbl_M_MovtosInventario(models.Model):
# Movimientos  Inventario)
    IDMovimiento = models.IntegerField(blank= False,null= False,help_text='Consecutivo numerico')
    IDPeriodo  = models.IntegerField(blank= False,null= False,
                      choices =ESTATUS_PERIODO_TYPE_Tuples)  
                       #MES, ANIO
    IDPlanProducción = models.CharField(max_length=30,blank=False, null=False,
                       help_text='Ingrese su Clave dePlan produccion recomendacion ddmmaa')
    IDVenta = models.IntegerField(blank= False,null= False,help_text='Consecutivo del maestro de ventas')
    IDCompra  = models.IntegerField(blank= False,null= False,help_text='Consecutivo del maestro de compras')
    IDTipoMovimiento = models.IntegerField(blank= False,null= False,help_text='SOLO ELIGE TIPO MOVIMIENTO')
    NombreProducto = models.ForeignKey(Cat_M_Inventario, null= False, blank = False,
                  on_delete = models.CASCADE,help_text='Ingrese Nombre Producto',
                  )
   # models.CharField(max_length=150,blank=False,null=False)    
    FechaMovto = models.DateTimeField(default=timezone.now)
    Cantidad = models.DecimalField(blank=True, null=False, default= 0,
                   max_digits=2,decimal_places=0) 
    Observaciones = models.CharField(max_length=150,blank=False,null=False)    
    IdEmpleado = models.CharField(max_length=30,blank=False,null=False)    
    ctlusuario = models.CharField(max_length=30,blank=False,null=False)    
    ctlfecha = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.NombreProducto


class Tbl_M_Formula(models.Model):
# Maestro de formulas
    IDFormula = models.CharField(max_length=30,blank=False, null=False,
                    primary_key = True ,help_text='Ingrese su Clave de Formula')
    NombreProducto = models.ForeignKey(Cat_M_Inventario, null= False, blank = False,
                    on_delete = models.CASCADE,help_text='Ingrese Nombre Producto',
                    )
    NumeroPiezas = models.IntegerField(blank= False,null= False)
    NombreResponsable = models.CharField(max_length=30,blank=False, null=False,
                    help_text='Ingrese Nombre Responsable',
                    )
    EstatusFormula = models.IntegerField(blank= False,null= False,
                      choices =FORMULA_TYPE_Tuples)  
    FechaLiberacion = models.DateTimeField(default=timezone.now)
    kilosMermaAprox = models.DecimalField()
    Observaciones = models.TextField()    
    ctlusuario = models.CharField(max_length=30,blank=False,null=False)    
    ctlfecha = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.IDFormula

class Tbl_D_Formula(models.Model):
# Detalle de formulas
    IDFormula = models.ForeignKey(Tbl_M_Formula, null= False, blank = False,
                    on_delete = models.CASCADE,help_text='Ingrese Id de Formula',
                    )
    NombreProducto = models.ForeignKey(Cat_M_Inventario, null= False, blank = False,
                  on_delete = models.CASCADE,help_text='Ingrese Nombre Producto',
                  )
    Cantidad = models.DecimalField(blank=True, null=False, default= 0,
                       max_digits=11,decimal_places=2)
    NombreResponsable = models.CharField(max_length=30,blank=False, null=False,
                    help_text='Ingrese Nombre Responsable',
                    )
    
    FechaLiberacion = models.DateTimeField(default=timezone.now)
    kilosMermaAprox = models.DecimalField(blank=True, null=False, default= 0,
                       max_digits=11,decimal_places=2)
    Observaciones = models.TextField()    
    ctlusuario = models.CharField(max_length=30,blank=False,null=False)    
    ctlfecha = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.IDFormula