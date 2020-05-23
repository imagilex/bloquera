from django.shortcuts import render
from django.views import View

from .cat_m_empleado_forms import frmCat_M_Empleado as base_form
from .models import Cat_M_Empleado as main_model

from zend_django.views import GenericCreate
from zend_django.views import GenericDelete
from zend_django.views import GenericList
from zend_django.views import GenericRead
from zend_django.views import GenericUpdate

from django.db.models import Q


def template_base_path(file):
    return 'catalogos/cat_m_empleado/' + file + ".html"

class List(GenericList):
    html_template = template_base_path("list")
    titulo = "Empleado"
    titulo_descripcion = "Catalogo"
    main_data_model = main_model
    model_name = "cat_m_empleado"

    def get_data(self, search_value=''):
        if '' == search_value:
            return list(
                self.main_data_model.objects.all())
        else:
            return list(self.main_data_model.objects.filter(
                Q(IDEmpleado__icontains=search_value) | Q(NombreEmpleado__icontains=search_value)))

class Read(GenericRead):
    titulo_descripcion = "Empleado"
    model_name = "cat_m_empleado"
    base_data_form = base_form
    main_data_model = main_model


class Create(GenericCreate):
    titulo = "Empleado"
    model_name = 'cat_m_empleado'
    base_data_form = base_form


class Update(GenericUpdate):
    titulo = "Empleado"
    model_name = "cat_m_empleado"
    base_data_form = base_form
    main_data_model = main_model


class Delete(GenericDelete):
    model_name = "cat_m_empleado"
    main_data_model = main_model