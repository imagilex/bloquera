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
    