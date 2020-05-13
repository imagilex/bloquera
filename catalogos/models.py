from django.db import models
from django.utils import timezone

# Inicio creacion de modelos.
# estos son parametros de imagefield adicionales,height_field=None
             #width_field=None) positiveintegerField
             #db_index = true en campos que son indices
#PrimaryKey('.IDProUser', on_delete=models.CASCADE)

class Cat_M_MateriaPrima(models.Model):
    IDProducto = models.CharField(max_length=30,blank=False, null=False,
                 primary_key = True ,help_text='Ingrese su Clave de Producto')
    NombreProducto=models.CharField(max_length=150,blank=False,null=False)    
    IDFoto = models.ImageField(max_length=110,upload_to='Pictures',null=True)
    FechaAlta = models.DateTimeField(default=timezone.now)
    UnidadMedida=models.CharField(max_length=10)
    ExistenciaActual = models.DecimalField(blank=True, null=False, default= 0,
                       max_digits=11,decimal_places=2)
                       #models.TextField()
 #   created_date =
    def __str__(self):
        return self.NombreProducto


class Cat_M_Inventarios(models.Model):
    IDProducto = models.CharField(max_length=30,blank=False, null=False,
                 primary_key = True ,help_text='Ingrese su Clave de Producto')
    #Id producto terminado, Id materia prima y mezclas
    IDTipoProducto = models.DecimalField(blank=True, null=False, default= 0, 
                     max_digits=2,decimal_places=0) 
    #-Producto Terminado, Materia Prima, Mezcla
    NombreProducto=models.CharField(max_length=150,blank=False,null=False)    
    IDFoto = models.ImageField(max_length=110,upload_to='Pictures',null=True)
    FechaAlta = models.DateTimeField(default=timezone.now)
    UnidadMedida=models.CharField(max_length=10)
    ExistenciaActual = models.DecimalField(blank=True, null=False, default= 0,
                       max_digits=11,decimal_places=2)
    ExistenciaMaxima = models.DecimalField(blank=True, null=False, default= 0,
                       max_digits=11,decimal_places=2)
    ExistenciaMinima = models.DecimalField(blank=True, null=False, default= 0,
                       max_digits=11,decimal_places=2)
    Observaciones =models.CharField(max_length=150,blank=False,null=False)    
    DiasPromedioResurtimiento =models.DecimalField(blank=True, null=False, default= 0,
                       max_digits=2,decimal_places=0) 
    Produccionmaxdia = models.DecimalField(blank=True, null=False, default= 0,
                       max_digits=2,decimal_places=0) 
    CostoUnitarioultimaProducción =  models.DecimalField(blank=True, null=False, default= 0,
                       max_digits=2,decimal_places=0) 
    Preciocostoultimacompra =  models.DecimalField(blank=True, null=False, default= 0,
                       max_digits=2,decimal_places=0) 
    Preciovtaultimaproduccion = models.DecimalField(blank=True, null=False, default= 0,
                       max_digits=2,decimal_places=0) 
    Preciovtaunitarioultimaproduccion = models.DecimalField(blank=True, null=False, default= 0,
                       max_digits=2,decimal_places=0) 
    ctlusuario =models.CharField(max_length=30,blank=False,null=False)    
    ctlFecha  = models.DateTimeField(default=timezone.now)

def __str__(self):
        return self.NombreProducto
    
class Tbl_M_MovtosInventario(models.Model):
# Movimientos  Inventario)
    IDPeriodo  = models.IntegerField(blank= False,null= False,help_text='Ingrese 99-mes-99anio')
    IDMovimiento = models.IntegerField(blank= False,null= False,help_text='Consecutivo numerico')
    IDProducto = models.CharField(max_length=30,blank=False, null=False,
                 primary_key = True ,help_text='Ingrese su Clave de Producto')
    IDPlanProducción = models.CharField(max_length=30,blank=False, null=False,
                       help_text='Ingrese su Clave dePlan produccion recomendacion ddmmaa')
    IDVentaIDMovimiento = models.IntegerField(blank= False,null= False,help_text='Consecutivo del maestro de ventas')
    IDCompra  = models.IntegerField(blank= False,null= False,help_text='Consecutivo del maestro de compras')
    IDTipoMovimiento = models.IntegerField(blank= False,null= False,help_text='SOLO ELIGE TIPO MOVIMIENTO')
    FechaMovto = models.DateTimeField(default=timezone.now)
    Cantidad = models.DecimalField(blank=True, null=False, default= 0,
                       max_digits=2,decimal_places=0) 
    Observaciones = models.CharField(max_length=150,blank=False,null=False)    
    IdEmpleado = models.CharField(max_length=30,blank=False,null=False)    
    ctlusuario =models.CharField(max_length=30,blank=False,null=False)    
    ctlfecha = models.DateTimeField(default=timezone.now)

def __str__(self):
        return self.IDProducto

