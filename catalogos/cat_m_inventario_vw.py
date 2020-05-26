from django.shortcuts import render
from django.views import View

from .cat_m_inventario_forms import frmCat_M_Inventario as base_form
from .models import Cat_M_Inventario as main_model

from zend_django.views import GenericCreate
from zend_django.views import GenericDelete
from zend_django.views import GenericList
from zend_django.views import GenericRead
from zend_django.views import GenericUpdate

from django.db.models import Q

def template_base_path(file):
    return 'catalogos/cat_m_inventario/' + file + ".html"

class List(GenericList):
    html_template = template_base_path("list")
    titulo = "Inventario"
    titulo_descripcion = "Catalogo"
    main_data_model = main_model
    model_name = "cat_m_inventario"

    def get_data(self, search_value=''):
        if '' == search_value:
            return list(
                self.main_data_model.objects.all())
        else:
            return list(self.main_data_model.objects.filter(
                Q(IDProducto__icontains=search_value) | Q(NombreProducto__icontains=search_value)))

class Read(GenericRead):
    titulo_descripcion = "Inventario"
    model_name = "cat_m_inventario"
    base_data_form = base_form
    main_data_model = main_model


class Create(GenericCreate):
    titulo = "Inventario"
    model_name = 'cat_m_inventario'
    base_data_form = base_form


class Update(GenericUpdate):
    titulo = "Inventario"
    model_name = "cat_m_inventario"
    base_data_form = base_form
    main_data_model = main_model


class Delete(GenericDelete):
    model_name = "cat_m_inventario"
    main_data_model = main_model
