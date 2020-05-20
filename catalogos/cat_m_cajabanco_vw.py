from django.shortcuts import render
from django.views import View
from django.db.models import Q
from .cat_m_cajabanco_forms import frmCat_M_CajaBanco as base_form
from .models import Cat_M_CajaBanco as main_model

from zend_django.views import GenericCreate
from zend_django.views import GenericDelete
from zend_django.views import GenericList
from zend_django.views import GenericRead
from zend_django.views import GenericUpdate

def template_base_path(file):
    return 'catalogos/cat_m_cajabanco/' + file + ".html"

class List(GenericList):
    html_template = template_base_path("list")
    titulo = "Caja_banco"
    titulo_descripcion = "Caja Banco"
    main_data_model = main_model
    model_name = "cat_m_cajabanco"

    def get_data(self, search_value=''):
        if '' == search_value:
            return list(
                self.main_data_model.objects.all())
        else:
            return list(self.main_data_model.objects.filter(
                Q(IDCajaBanco__icontains=search_value) | Q(Nombre__icontains=search_value)))

class Read(GenericRead):
    titulo_descripcion = "Caja_banco"
    model_name = "cat_m_cajabanco"
    base_data_form = base_form
    main_data_model = main_model


class Create(GenericCreate):
    titulo = "Caja_banco"
    model_name = 'cat_m_cajabanco'
    base_data_form = base_form


class Update(GenericUpdate):
    titulo = "Caja_banco"
    model_name = "cat_m_cajabanco"
    base_data_form = base_form
    main_data_model = main_model

class Delete(GenericDelete):
    model_name = "cat_m_cajabanco"
    main_data_model = main_model