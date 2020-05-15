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
    NombreProducto = models.CharField(max_length=150,blank=False,null=False)    
    IDFoto = models.ImageField(max_length=110,upload_to='Pictures',null=True)
    FechaAlta = models.DateTimeField(default=timezone.now)
    UnidadMedida = models.CharField(max_length=10)
    ExistenciaActual = models.DecimalField(blank=True, null=False, default= 0,
                       max_digits=11,decimal_places=2)
                       #models.TextField()
 #   created_date =
    def __str__(self):
        return self.NombreProducto

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
    Cantidad = models.DecimalField(blank=True, null=False, default= 0,max_digits=2,decimal_places=0) 
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
    NombreProveedor = models.CharField(max_length=150,blank=False,null=False)    
    Empresa = models.CharField(max_length=50,blank=False,null=False)    
    Rfc = models.CharField(max_length=150,blank=False,null=False)    
    DirFiscal = models.CharField(max_length=150,blank=False,null=False)    
    Telefono1 = models.CharField(max_length=50,blank=False,null=False)    
    Telefono2 = models.CharField(max_length=50,blank=False,null=False)    
    Telefono3 = models.CharField(max_length=50,blank=False,null=False)
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
    Telefono2 = models.CharField(max_length=50,blank=False,null=False)    
    Telefono3 = models.CharField(max_length=50,blank=False,null=False)
    Comentarios = models.TextField()    
    ctlusuario = models.CharField(max_length=30,blank=False,null=False)    
    ctlfecha = models.DateTimeField(default=timezone.now)

def __str__(self):
         return self.NombreContacto

class Cat_M_Clientes(models.Model):
#Catalogo Cientes
    IDCliente = models.CharField(max_length=30,blank=False, null=False,
                       primary_key = True ,help_text='Ingrese Clave de Cliente')
    NombreCliente = models.CharField(max_length=150,blank=False,null=False)    
    NombreProveedor = models.CharField(max_length=150,blank=False,null=False)    
    Empresa = models.CharField(max_length=50,blank=False,null=False)    
    Rfc = models.CharField(max_length=150,blank=False,null=False)    
    DirFiscal = models.CharField(max_length=150,blank=False,null=False)    
    Email = models.EmailField()     
    Telefono1 = models.CharField(max_length=50,blank=False,null=False)    
    Telefono2 = models.CharField(max_length=50,blank=False,null=False)    
    Telefono3 = models.CharField(max_length=50,blank=False,null=False) 
    ctlusuario = models.CharField(max_length=30,blank=False,null=False)    
    ctlFecha  = models.DateTimeField(default=timezone.now)

def __str__(self):
         return self.NombreCliente


    
class Cat_D_ClientesSucursales(models.Model):
#Contactos Proveedores
    IDCliente = models.ForeignKey(Cat_M_Clientes, null= False, blank = False,
                  on_delete = models.CASCADE,help_text='Ingrese Clave de Cliente',
                  )
    NombreContacto = models.CharField(max_length=100,blank=False,null=False)    
    Cargo = models.CharField(max_length=50,blank=False,null=False)    
    Sucursal = models.CharField(max_length=50,blank=False,null=False)
    Direccion = models.TextField()    
    Email = models.EmailField()    
    Telefono1 = models.CharField(max_length=50,blank=False,null=False)    
    Telefono2 = models.CharField(max_length=50,blank=False,null=False)    
    Telefono3 = models.CharField(max_length=50,blank=False,null=False)
    Comentarios = models.TextField()    
    ctlusuario = models.CharField(max_length=30,blank=False,null=False)    
    ctlfecha = models.DateTimeField(default=timezone.now)

def __str__(self):
         return self.NombreContacto



#Catalogo Prospectos
#	Id Prospecto
#	Nombre Completo
#	ID Tipo Prospecto (Llego directo, Buscado)
#	Para que necesita el material?
#	Es constructora?
#	Es casa de materiales?
#	Que productos le interesan?
#	Cantidad requerida?
#	Fecha Registro
#	Id Vendedor
#	Id Publicidad
#	Puesto
#    E-mail = models.EmailField()    
#    Telefono1 = models.CharField(max_length=50,blank=False,null=False)    
#    Telefono2 = models.CharField(max_length=50,blank=False,null=False)    
#    Telefono3 = models.CharField(max_length=50,blank=False,null=False)
#	Dirección Fiscal
#	Datos Fiscales Facturación
#	Dirección Entrega 1
#	Dirección Entrega 2
#	Dirección Entrega 3
#	Ultima Fecha Envió Catalogo
#	Estatus
#	Comentarios
#    ctlusuario = models.CharField(max_length=30,blank=False,null=False)    
#    ctlFecha  = models.DateTimeField(default=timezone.now)

#Detalle SeguimientoProspectos
#	Id Prospecto
#	Fecha Seguimiento
#	Próxima Fecha seguimiento
#	Descripción Acuerdos
#    ctlusuario = models.CharField(max_length=30,blank=False,null=False)    
#    ctlFecha  = models.DateTimeField(default=timezone.now)

#Catalogo Empleados
#	ID Empleado
#	ID HUELLA
#	Nombre
#	ID FOTO
#	Dirección
#	IMSS
#	Rfc
#    E-mail = models.EmailField()    
#    Telefono1 = models.CharField(max_length=50,blank=False,null=False)    
#	Periodo Pago (Días)
#	Sueldo
#	Tipo Empleado (Semanal/Quincenal)
#	Horas extra(SI/NO)
#	Área
#	Monto por hora extra
#	Puesto
#    ctlusuario = models.CharField(max_length=30,blank=False,null=False)    
#    ctlFecha  = models.DateTimeField(default=timezone.now)


#Catalogo Fletes
#	ID Flete
#	Nombre
#	Capacidad Mínima Tarimas
#	Capacidad Máxima Tarimas
#	Precio
#	Kilómetros Distancia
#	ID Proveedor
#	Zona Estado
#	Zona Municipios
#	Días Hábiles
#	Comentarios
#    ctlusuario = models.CharField(max_length=30,blank=False,null=False)    
#    ctlFecha  = models.DateTimeField(default=timezone.now)

#Catalogo Vendedores
#	ID Vendedor
#	Nombre
#	RFC
#	Domicilio Fiscal
#	Dirección
#    E-mail = models.EmailField()    
#    Telefono1 = models.CharField(max_length=50,blank=False,null=False)    
#    Telefono2 = models.CharField(max_length=50,blank=False,null=False)    
#	Zona Estado
#	Zona Municipio
#	Comentarios
#    ctlusuario = models.CharField(max_length=30,blank=False,null=False)    
#    ctlFecha  = models.DateTimeField(default=timezone.now)

#Catalogo Cajas Bancos
#	ID Caja Banco
#	Descripción
#	Sucursal Alta
#	Dirección
#	Numero Cuenta
#	Nombre Banco
#    EmailEjecutivo = models.EmailField()    
#    Telefono1 = models.CharField(max_length=50,blank=False,null=False)    
#    Telefono2 = models.CharField(max_length=50,blank=False,null=False)    
    #	Clabe interbancaria
#	Nombre Titular
#	Tipo Cuenta
#	Responsable
#    ctlusuario = models.CharField(max_length=30,blank=False,null=False)    
#    ctlFecha  = models.DateTimeField(default=timezone.now)


