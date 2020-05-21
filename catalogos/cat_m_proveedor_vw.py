from django.shortcuts import render
from django.views import View
from django.db.models import Q
from .cat_m_proveedor_forms import frmCat_M_Proveedor as base_form
from .models import Cat_M_Proveedor as main_model

from zend_django.views import GenericCreate
from zend_django.views import GenericDelete
from zend_django.views import GenericList
from zend_django.views import GenericRead
from zend_django.views import GenericUpdate

def template_base_path(file):
    return 'catalogos/cat_m_proveedor/' + file + ".html"

class List(GenericList):
    html_template = template_base_path("list")
    titulo = "Proveedores"
    titulo_descripcion = "Catalogo Proveedores"
    main_data_model = main_model
    model_name = "cat_m_proveedor"

    def get_data(self, search_value=''):
        if '' == search_value:
            return list(
                self.main_data_model.objects.all())
        else:
            return list(self.main_data_model.objects.filter(
                Q(IDProveedor__icontains=search_value) | Q(NombreProveedor__icontains=search_value)))

class Read(GenericRead):
    titulo_descripcion = "Proveedores"
    model_name = "cat_m_proveedor"
    base_data_form = base_form
    main_data_model = main_model


class Create(GenericCreate):
    titulo = "Proveedores"
    model_name = 'cat_m_proveedor'
    base_data_form = base_form


class Update(GenericUpdate):
    titulo = "Proveedores"
    model_name = "cat_m_proveedor"
    base_data_form = base_form
    main_data_model = main_model


class Delete(GenericDelete):
    model_name = "cat_m_proveedor"
    main_data_model = main_model



