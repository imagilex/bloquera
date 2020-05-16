from django.urls import include
from django.urls import path

urlpatterns = [
    path('materia_prima/', include('catalogos.cat_m_materiaprima_urls')),
    path('inventario/', include('catalogos.cat_m_inventario_urls')),
    path('movimientos_inventario/', include('catalogos.tbl_m_movtosinventario_urls')),
    path('proveedores/', include('catalogos.cat_m_proveedores_urls')),
    path('proveedores_contactos/', include('catalogos.cat_d_proveedorescontactos_urls')),
    path('clientes/', include('catalogos.cat_m_clientes_urls')),
    path('clientes_contactos/', include('catalogos.cat_d_clientessucursales_urls')),
    path('vendedor/', include('catalogos.cat_m_vendedor_urls')),
    path('prospecto/', include('catalogos.cat_m_prospecto_urls')),
    path('prospecto_detalle/', include('catalogos.cat_d_prospecto_urls')),
    path('flete/', include('catalogos.cat_m_flete_urls')),
    path('caja_banco/', include('catalogos.cat_m_cajabanco_urls')),

]
