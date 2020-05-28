from django.shortcuts import render
from django.views import View

from .cat_m_flete_forms import frmCat_M_Flete as base_form
from .models import Cat_M_Flete as main_model

from zend_django.views import GenericCreate
from zend_django.views import GenericDelete
from zend_django.views import GenericList
from zend_django.views import GenericRead
from zend_django.views import GenericUpdate

from django.db.models import Q

def template_base_path(file):
    return 'catalogos/cat_m_flete/' + file + ".html"

class List(GenericList):
    html_template = template_base_path("list")
    titulo = "Fletes"
    titulo_descripcion = "Catalogo"
    main_data_model = main_model
    model_name = "cat_m_flete"

    def get_data(self, search_value=''):
            if '' == search_value:
                return list(
                    self.main_data_model.objects.all())
            else:
                return list(self.main_data_model.objects.filter(
                    Q(IDFlete__icontains=search_value) | Q(NombreFlete__icontains=search_value)))

class Read(GenericRead):
    titulo_descripcion = "Fletes"
    model_name = "cat_m_flete"
    base_data_form = base_form
    main_data_model = main_model

class Create(GenericCreate):
    titulo = "Fletes"
    model_name = 'cat_m_flete'
    base_data_form = base_form


class Update(GenericUpdate):
    titulo = "Fletes"
    model_name = "cat_m_flete"
    base_data_form = base_form
    main_data_model = main_model


class Delete(GenericDelete):
    model_name = "cat_m_flete"
    main_data_model = main_model