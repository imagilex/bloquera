from django.db import models
from django.utils import timezone


# Inicio creacion de modelos.
# estos son parametros de imagefield adicionales,height_field=None
             #width_field=None) positiveintegerField
             #db_index = true en campos que son indices
#PrimaryKey('.IDProUser', on_delete=models.CASCADE)

STATUS_TYPE = {
    'VIGENTE': 'VIGENTE',
    'DESCONTINUADO': 'DESCONTINUADO',
    'CANCELADO': 'CANCELADO',
    'SUSPENDIDO': 'SUSPENDIDO',
    
}

STATUS_TYPE_Tuples = (
        (STATUS_TYPE['VIGENTE'], 'VIGENTE'),
        (STATUS_TYPE['DESCONTINUADO'], 'DESCONTINUADO'),
        (STATUS_TYPE['CANCELADO'], 'CANCELADO'),
        (STATUS_TYPE['SUSPENDIDO'], 'SUSPENDIDO'),
        
    )

IDPRODUCTO_TYPE = {
    'PRODCUCTO_TERMINADO': 'PRODCUCTO TERMINADO',
    'MATERIA_PRIMA': 'MATERIA PRIMA',
    'MATERIAL_EN_PROCESO': 'MATERIAL EN PROCESO',
}

IDPRODUCTO_TYPE_Tuples = (
        (IDPRODUCTO_TYPE['PRODCUCTO_TERMINADO'], 'PRODCUCTO TERMINADO'),
        (IDPRODUCTO_TYPE['MATERIA_PRIMA'], 'MATERIA PRIMA'),
        (IDPRODUCTO_TYPE['MATERIAL_EN_PROCESO'], 'MATERIAL EN PROCESO'),
    )

CAPTACION_CTE_TYPE = {
    'DIRECTO': 'DIRECTO',
    'VENDEDOR': 'VENDEDOR',
    'PAGINA_WEB': 'PAGINA_WEB',
    'OTROS': 'OTROS',
}

CAPTACION_CTE_TYPE_Tuples = (
        (CAPTACION_CTE_TYPE['DIRECTO'], 'DIRECTO'),
        (CAPTACION_CTE_TYPE['VENDEDOR'], 'VENDEDOR'),
        (CAPTACION_CTE_TYPE['PAGINA_WEB'], 'PAGINA_WEB'),
        (CAPTACION_CTE_TYPE['OTROS'], 'OTROS'),
    )

SINO_TYPE = {
    'SI': 'SI',
    'NO': 'NO',
}

SINO_TYPE_Tuples = (
        (SINO_TYPE['SI'], 'SI'),
        (SINO_TYPE['NO'], 'NO'),
    )

ESTATUS_PROSPECTO_TYPE = {
    'VIGENTE': 'VIGENTE',
    'CANCELADO': 'CANCELADO',
    'ALTA_CLIENTE': 'ALTA_CLIENTE',
}

ESTATUS_PROSPECTO_TYPE_Tuples = (
        (ESTATUS_PROSPECTO_TYPE['VIGENTE'], 'SI'),
        (ESTATUS_PROSPECTO_TYPE['CANCELADO'], 'NO'),
        (ESTATUS_PROSPECTO_TYPE['ALTA_CLIENTE'], 'ALTA_CLIENTE'),
    )



class Cat_M_Inventario(models.Model):
    IDProducto = models.CharField(max_length=30,blank=False, null=False,
                       primary_key = True ,help_text='Ingrese su Clave de Producto')
    IDTipoProducto = models.CharField(max_length=30,blank=False, null=False,
                       default= "PRODUCTO TERMINADO",choices = IDPRODUCTO_TYPE_Tuples ) 
    #-Producto Terminado, Materia Prima, Mezcla
    NombreProducto = models.CharField(max_length=150,blank=False,null=False)    
    IDFoto = models.ImageField(max_length=110,upload_to='Pictures',null=True)
    FechaAlta = models.DateTimeField(default=timezone.now)
    UnidadMedida = models.CharField(max_length=10)
    ExistenciaActual = models.DecimalField(blank=True, null=False, default= 0,
                       max_digits=11,decimal_places=2)
    ExistenciaMaxima = models.DecimalField(blank=True, null=False, default= 0,
                       max_digits=11,decimal_places=2)
    ExistenciaMinima = models.DecimalField(blank=True, null=False, default= 0,
                       max_digits=11,decimal_places=2)
    Observaciones = models.CharField(max_length=150,blank=False,null=False)    
    DiasPromedioResurtimiento = models.DecimalField(blank=True, null=False, default= 0,
                       max_digits=3,decimal_places=0) 
    Produccionmaxdia = models.DecimalField(blank=True, null=False, default= 0,
                       max_digits=6,decimal_places=0) 
    CostoUnitarioultimaProducción =  models.DecimalField(blank=True, null=False, default= 0,
                       max_digits=8,decimal_places=2)
    Preciocostoultimacompra =  models.DecimalField(blank=True, null=False, default= 0,
                       max_digits=8,decimal_places=2) 
    Preciovtaultimaproduccion = models.DecimalField(blank=True, null=False, default= 0,
                       max_digits=8,decimal_places=2) 
    Preciovtaunitarioultimaproduccion = models.DecimalField(blank=True, null=False, default= 0,
                       max_digits=8,decimal_places=2) 
    Status = models.CharField(blank=False, null=False, max_length=20,
                       default = "VIGENTE", choices = STATUS_TYPE_Tuples )
                       #VIGENTE,DESCONTINUADO,CANCELADO Y SUSPENDIDO
    ctlusuario = models.CharField(max_length=30,blank=False,null=False)    
    ctlFecha  = models.DateTimeField(default=timezone.now)

def __str__(self):
        return self.NombreProducto
    
class Tbl_M_MovtosInventario(models.Model):
# Movimientos  Inventario)
    IDPeriodo  = models.IntegerField(blank= False,null= False,help_text='Ingrese 99-mes-99anio')
    IDMovimiento = models.IntegerField(blank= False,null= False,help_text='Consecutivo numerico')
    IDProducto = models.CharField(max_length=30,blank=False, null=False, primary_key = True ,help_text='Ingrese su Clave de Producto')
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
    ctlusuario = models.CharField(max_length=30,blank=False,null=False)    
    ctlfecha = models.DateTimeField(default=timezone.now)

def __str__(self):
        return self.IDProducto

class Cat_M_Proveedores(models.Model):
#Catalogo Proveedores
    IDProveedor = models.CharField(max_length=30,blank=False, null=False,
                       primary_key = True ,help_text='Ingrese Clave de Proveedor')
    NombreProveedor = models.CharField(max_length=100,blank=False,null=False)    
    Empresa = models.CharField(max_length=100,blank=False,null=False)    
    Rfc = models.CharField(max_length=30,blank=False,null=False)    
    DirFiscal = models.CharField(max_length=150,blank=False,null=False)    
    Telefono1 = models.CharField(max_length=50,blank=False,null=False)    
    Telefono2 = models.CharField(max_length=50,blank=True,null=False)    
    Telefono3 = models.CharField(max_length=50,blank=True,null=False)
    Email = models.EmailField()
    ctlusuario = models.CharField(max_length=30,blank=False,null=False)    
    ctlfecha = models.DateTimeField(default=timezone.now)

def __str__(self):
        return self.NombreProveedor

class Cat_D_ProveedoresContactos(models.Model):
#Contactos Proveedores
    IDProveedor = models.ForeignKey(Cat_M_Proveedores, null= False, blank = False,
                  on_delete = models.CASCADE,help_text='Ingrese Clave de Proveedor',
                  )
    NombreContacto = models.CharField(max_length=100,blank=False,null=False)    
    CargoContacto = models.CharField(max_length=50,blank=False,null=False)    
    SucursalContacto = models.CharField(max_length=50,blank=False,null=False)
    DireccionContacto = models.TextField()    
    Email = models.EmailField()    
    Telefono1 = models.CharField(max_length=50,blank=False,null=False)    
    Telefono2 = models.CharField(max_length=50,blank=True,null=False)    
    Telefono3 = models.CharField(max_length=50,blank=True,null=False)
    Comentarios = models.TextField()    
    ctlusuario = models.CharField(max_length=30,blank=False,null=False)    
    ctlfecha = models.DateTimeField(default=timezone.now)

def __str__(self):
         return self.NombreContacto

class Cat_M_Clientes(models.Model):
#Catalogo Cientes
    IDCliente = models.CharField(max_length=30,blank=False, null=False,
                       primary_key = True ,help_text='Ingrese Clave de Cliente')
    NombreCliente = models.CharField(max_length=100,blank=False,null=False)    
    NombreProveedor = models.CharField(max_length=100,blank=False,null=False)    
    Empresa = models.CharField(max_length=100,blank=False,null=False)    
    Rfc = models.CharField(max_length=30,blank=False,null=False)
    DirFiscal = models.CharField(max_length=150,blank=False,null=False)    
    Email = models.EmailField()     
    Telefono1 = models.CharField(max_length=50,blank=False,null=False)    
    Telefono2 = models.CharField(max_length=50,blank=True,null=False)    
    Telefono3 = models.CharField(max_length=50,blank=True,null=False)
    ctlusuario = models.CharField(max_length=30,blank=False,null=False)    
    ctlFecha  = models.DateTimeField(default=timezone.now)

def __str__(self):
         return self.NombreCliente
  
class Cat_D_ClientesSucursales(models.Model):
#Clientes Sucursales
    IDCliente = models.ForeignKey(Cat_M_Clientes, null= False, blank = False,
                  on_delete = models.CASCADE,help_text='Ingrese Clave de Cliente',
                  )
    NombreContacto = models.CharField(max_length=100,blank=False,null=False)
    Cargo = models.CharField(max_length=50,blank=False,null=False)    
    Sucursal = models.CharField(max_length=50,blank=False,null=False)
    Direccion = models.TextField()
    Email = models.EmailField()
    Telefono1 = models.CharField(max_length=50,blank=False,null=False)    
    Telefono2 = models.CharField(max_length=50,blank=True,null=False)    
    Telefono3 = models.CharField(max_length=50,blank=True,null=False)
    Comentarios = models.TextField()
    ctlusuario = models.CharField(max_length=30,blank=False,null=False)    
    ctlfecha = models.DateTimeField(default=timezone.now)

def __str__(self):
         return self.NombreContacto

class Cat_M_Vendedor(models.Model):
#Catalogo Vendedores
    IDVendedor = models.CharField(max_length=30,blank=False, null=False,
                       primary_key = True ,help_text='Ingrese Clave de Vendedor')
    NombreVendedor = models.CharField(max_length=100,blank=False,null=False)
    Direccion = models.TextField()
    Rfc = models.CharField(max_length=30,blank=False,null=False)
    Email = models.EmailField()
    Telefono1 = models.CharField(max_length=50,blank=False,null=False)    
    Telefono2 = models.CharField(max_length=50,blank=True,null=False)    
    Telefono3 = models.CharField(max_length=50,blank=True,null=False)
    Comentarios = models.TextField()
    ctlusuario = models.CharField(max_length=30,blank=False,null=False)    
    ctlfecha = models.DateTimeField(default=timezone.now)



class Cat_M_Prospecto(models.Model):
#Catalogo Prospectos
    IDProspecto = models.CharField(max_length=30,blank=False, null=False,
                       primary_key = True ,help_text='Ingrese Clave Prospecto')
    Nombre = models.CharField(max_length=100,blank=False,null=False)
    TipoCaptacion = models.CharField(max_length=30,blank=False, null=False,
                       default= "DIRECTO",choices = CAPTACION_CTE_TYPE_Tuples ) 
                      #'DIRECTO', 'VENDEDOR','PAGINA_WEB', 'OTROS',
    UsoMaterial = models.CharField(max_length=40,blank=False, null=False,
                       help_text='Para que necesita el material?' )
    Constructora = models.CharField(max_length=40,blank=True, null=True,
                       help_text='Nombre Constructora' )
    CasaMateriales = models.CharField(max_length=40,blank=True, null=True,
                       help_text='Nombre Casa Materiales' )
    ProductosInteres = models.TextField( help_text='Productos de Interes, Incluyendo Cantidades')
    FechaRegistro = models.DateTimeField(default=timezone.now)
    NombreVendedor = models.ForeignKey(Cat_M_Vendedor, null= False, blank = False,
                  on_delete = models.CASCADE,help_text='Ingrese Vendedor',
                  )
    Puesto = models.CharField(max_length=50,blank=True, null=True)
    Email = models.EmailField()
    Telefono1 = models.CharField(max_length=50,blank=False,null=False)
    Telefono2 = models.CharField(max_length=50,blank=True,null=False)    
    Telefono3 = models.CharField(max_length=50,blank=True,null=False)
    Direccion = models.TextField()
    Estatus = models.CharField(max_length=20,blank=False, null=False,
                       default= "VIGENTE",choices = ESTATUS_PROSPECTO_TYPE_Tuples ) 
#	Vigente, Cancelado,AltaCliente
    Comentarios = models.TextField()
    ctlusuario = models.CharField(max_length=30,blank=False,null=False)    
    ctlfecha = models.DateTimeField(default=timezone.now)

class Cat_D_Prospecto(models.Model):
#Detalle SeguimientoProspectos
    IDProspecto = models.ForeignKey(Cat_M_Vendedor, null= False, blank = True,
                  on_delete = models.CASCADE,help_text='Ingrese ID Prospecto',
                  )
    Nombre = models.CharField(max_length=100,blank=False,null=False)    
#	Id Prospecto
    FechaNota = models.DateTimeField(default=timezone.now)
    ProximoSeguimiento = models.DateTimeField(default=timezone.now)
#	Próxima Fecha seguimiento
    Seguimiento = models.TextField()
#	Descripción Acuerdos
    ctlusuario = models.CharField(max_length=30,blank=False,null=False)
    ctlfecha = models.DateTimeField(default=timezone.now)

class Cat_M_Empleado(models.Model):
#Catalogo Empleados
    IDEmpleado = models.CharField(max_length=30,blank=False, null=False,
                       primary_key = True ,help_text='Ingrese Clave Prospecto')
    Nombre = models.CharField(max_length=100,blank=False,null=False)
    Foto = models.ImageField(max_length=110,upload_to='Pictures',null=True)
    Direccion = models.TextField()
    NSS = models.CharField(max_length=30,blank=False,null=False)
    Rfc = models.CharField(max_length=30,blank=False,null=False)
    Email = models.EmailField()
    Telefono1 = models.CharField(max_length=50,blank=False,null=False)    
    PeriodoPago =  models.IntegerField(blank=True, null=False, default= 0,
                       help_text='Periodo Pago (Dias)' )
    Sueldo =  models.DecimalField(blank=True, null=False, default= 0,
                       max_digits=8,decimal_places=2)
    HorasExtra = models.CharField(max_length=20,blank=False, null=False,
                       default= "SI",choices = SINO_TYPE_Tuples ) 
#	Horas extra(SI/NO)
    Area = models.CharField(max_length=30,blank=False,null=False)    
    MontoHoraExtra =  models.DecimalField(blank=True, null=False, default= 0,
                       max_digits=8,decimal_places=2)
    Puesto = models.CharField(max_length=30,blank=False,null=False)    
    ctlusuario = models.CharField(max_length=30,blank=False,null=False)
    ctlfecha = models.DateTimeField(default=timezone.now)

class Cat_M_Flete(models.Model):
#Catalogo Fletes
    IDFlete = models.CharField(max_length=30,blank=False, null=False,
                       primary_key = True ,help_text='Ingrese Clave Flete')
    Nombre = models.CharField(max_length=100,blank=False,null=False)
    #	ID Proveedor
    NombreProveedor = models.ForeignKey(Cat_M_Proveedores, null= False, blank = True,
                  on_delete = models.CASCADE,
                  )
    CapacidadMinimaTarimas=  models.IntegerField(blank=True, null=False, default= 0)
    CapacidadMaximaTarimas=  models.IntegerField(blank=True, null=False, default= 0)
    Precio =  models.DecimalField(blank=True, null=False, default= 0,
                       max_digits=8,decimal_places=2)
    KilometrosMaxDistancia=  models.DecimalField(blank=True, null=False, default= 0,
                       max_digits=8,decimal_places=2)
    Comentarios = models.TextField()
    ctlusuario = models.CharField(max_length=30,blank=False,null=False)    
    ctlfecha = models.DateTimeField(default=timezone.now)

class Cat_M_CajaBanco(models.Model):
#Catalogo Cajas Bancos
    IDCajaBanco = models.CharField(max_length=30,blank=False, null=False,
                       primary_key = True ,help_text='Ingrese Clave Caja/Banco')
    Nombre = models.CharField(max_length=100,blank=False,null=False)
    Sucursal = models.CharField(max_length=50,blank=True,null=False)
    Direccion = models.CharField(max_length=100,blank=True,null=False)
    Num_CLABE = models.CharField(max_length=30,blank=True,null=False)
    Num_Cuenta = models.CharField(max_length=30,blank=True,null=False)
    Titular = models.CharField(max_length=30,blank=True,null=False)
    TipoCuenta = models.CharField(max_length=30,blank=True,null=False)
    NomBanco = models.CharField(max_length=30,blank=True,null=False)
    Ejecutivo = models.CharField(max_length=50,blank=True,null=False)
    Telefono1 = models.CharField(max_length=50,blank=True,null=False)
    Telefono2 = models.CharField(max_length=50,blank=True,null=False)    
    ctlusuario = models.CharField(max_length=30,blank=False,null=False)    
    ctlfecha = models.DateTimeField(default=timezone.now)
