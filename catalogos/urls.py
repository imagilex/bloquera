from django.contrib.auth.decorators import permission_required
from django.urls import include
from django.urls import path

from .vista_submenu_vw import SubMenu
import catalogos.vista_submenu_vw as views

urlpatterns = [
    path('inventario/', include('catalogos.cat_m_inventario_urls')),
    path('proveedores/', include('catalogos.cat_m_proveedor_urls')),
    path('proveedores_contactos/', include('catalogos.cat_d_proveedorcontacto_urls')),
    path('clientes/', include('catalogos.cat_m_cliente_urls')),
    path('clientes_sucursales/', include('catalogos.cat_d_clientesucursal_urls')),
    path('vendedor/', include('catalogos.cat_m_vendedor_urls')),
    path('prospectos/', include('catalogos.cat_m_prospecto_urls')),
    path('prospecto_detalle/', include('catalogos.cat_d_prospecto_urls')),
    path('flete/', include('catalogos.cat_m_flete_urls')),
    path('caja_banco/', include('catalogos.cat_m_cajabanco_urls')),
    path('empleados/', include('catalogos.cat_m_empleado_urls')),
    path('submenu/', SubMenu.as_view(),name="SubMenu"),
    #path('submenu', permission_required(catalogos.view_SubMenu')(views.List.as_view()),
     #   name=f"{SubMenu}_list"),

]