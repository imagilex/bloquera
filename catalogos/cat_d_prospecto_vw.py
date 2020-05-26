from django.shortcuts import render
from django.views import View

from .cat_d_prospecto_forms import frmCat_D_Prospecto as base_form
from .models import Cat_D_Prospecto as main_model

from zend_django.views import GenericCreate
from zend_django.views import GenericDelete
from zend_django.views import GenericList
from zend_django.views import GenericRead
from zend_django.views import GenericUpdate

from zend_django.parametros_models import ParametroUsuario
from django.db.models import Q

def template_base_path(file):
    return 'catalogos/cat_d_prospecto/' + file + ".html"

class List(GenericList):
    html_template = template_base_path("list")
    titulo = "Detalle del Prospecto"
    titulo_descripcion = "Catalogo"
    main_data_model = main_model
    model_name = "cat_d_prospecto"

    def get_data(self, pkprospecto, search_value=''):
        data = self.main_data_model.objects.filter(Prospecto__pk=pkprospecto)
       
        if '' == search_value:
            return list(
                data.all())
        else:
            return list(self.main_data_model.objects.filter(
                Q(Prospecto__icontains=search_value) | Q(FechaNota__icontains=search_value)))
    
    def get(self, request, pkprospecto):
            search_value = ParametroUsuario.get_valor(
                request.user, 'basic_search', self.model_name)
            return self.base_render(
                request, self.get_data(pkprospecto, search_value), search_value)

    def post(self, request, pkprospecto):
        if "search" == request.POST.get('action', ''):
            search_value = request.POST.get('valor', '')
        else:
            search_value = ParametroUsuario.get_valor(
                request.user, 'basic_search', self.model_name)
        return self.base_render(
            request, self.get_data(pkprospecto, search_value), search_value)

class Read(GenericRead):
    titulo_descripcion = "Detalle del Prospecto"
    model_name = "cat_d_prospecto"
    base_data_form = base_form
    main_data_model = main_model


class Create(GenericCreate):
    titulo = "Detalle del Prospecto"
    model_name = 'cat_d_prospecto'
    base_data_form = base_form


class Update(GenericUpdate):
    titulo = "Detalle del Prospecto"
    model_name = "cat_d_prospecto"
    base_data_form = base_form
    main_data_model = main_model


class Delete(GenericDelete):
    model_name = "cat_d_prospecto"
    main_data_model = main_model