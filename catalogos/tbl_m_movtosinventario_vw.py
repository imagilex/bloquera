from django.shortcuts import render
from django.views import View
from django.db.models import Q
from .tbl_m_movtosinventario_forms import frmTbl_M_MovtosInventario as base_form
from .models import Tbl_M_MovtosInventario as main_model

from zend_django.views import GenericCreate
from zend_django.views import GenericDelete
from zend_django.views import GenericList
from zend_django.views import GenericRead
from zend_django.views import GenericUpdate

def template_base_path(file):
    return 'catalogos/tbl_m_movtosinventario/' + file + ".html"

class List(GenericList):
    html_template = template_base_path("list")
    titulo = "Movimientos Inventario"
    titulo_descripcion = "Catalogo"
    main_data_model = main_model
    model_name = "tbl_m_movtosinventario"

    def get_data(self, search_value=''):
        if '' == search_value:
            return list(
                self.main_data_model.objects.all())
        else:
            return list(self.main_data_model.objects.filter(
                Q(IDProducto__icontains=search_value) | Q(IDMovimiento__icontains=search_value)))

class Read(GenericRead):
    titulo_descripcion = "Movimiento Inventario"
    model_name = "tbl_m_movtosinventario"
    base_data_form = base_form
    main_data_model = main_model

class Create(GenericCreate):
    titulo = "Movimiento Inventario"
    model_name = 'tbl_m_movtosinventario'
    base_data_form = base_form


class Update(GenericUpdate):
    titulo = "Movimiento Inventario"
    model_name = "tbl_m_movtosinventario"
    base_data_form = base_form
    main_data_model = main_model


class Delete(GenericDelete):
    model_name = "tbl_m_movtosinventario"
    main_data_model = main_model
