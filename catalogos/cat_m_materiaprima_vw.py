from django.shortcuts import render
from django.views import View

from .cat_m_materiaprima_forms import frmCat_M_MateriaPrima as base_form
from .models import Cat_M_MateriaPrima as main_model

from zend_django.views import GenericCreate
from zend_django.views import GenericDelete
from zend_django.views import GenericList
from zend_django.views import GenericRead
from zend_django.views import GenericUpdate

def template_base_path(file):
    return 'catalogos/cat_m_materiaprima/' + file + ".html"

class List(GenericList):
    html_template = template_base_path("list")
    titulo = "Materia Prima"
    titulo_descripcion = "Catalogo"
    main_data_model = main_model
    model_name = "cat_m_materiaprima"

    def get_data(self, search_value=''):
        if '' == search_value:
            return list(
                self.main_data_model.objects.all())
        else:
            return list(self.main_data_model.objects.filter(
                Q(IDProducto__icontains=search_value) | Q(NombreProducto__icontains=search_value)))

class Read(GenericRead):
    titulo_descripcion = "Materia Prima"
    model_name = "cat_m_materiaprima"
    base_data_form = base_form
    main_data_model = main_model


class Create(GenericCreate):
    titulo = "Materia Prima"
    model_name = 'cat_m_materiaprima'
    base_data_form = base_form


class Update(GenericUpdate):
    titulo = "Materia Prima"
    model_name = "cat_m_materiaprima"
    base_data_form = base_form
    main_data_model = main_model


class Delete(GenericDelete):
    model_name = "cat_m_materiaprima"
    main_data_model = main_model