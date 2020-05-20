from django.shortcuts import render
from django.views import View

from .cat_d_clientessucursales_forms import frmCat_D_ClientesSucursales as base_form
from .models import Cat_D_ClientesSucursales as main_model

from django.db.models import Q

from zend_django.views import GenericCreate
from zend_django.views import GenericDelete
from zend_django.views import GenericList
from zend_django.views import GenericRead
from zend_django.views import GenericUpdate

from zend_django.parametros_models import ParametroUsuario

def template_base_path(file):
    return 'catalogos/cat_d_clientessucursales/' + file + ".html"

class List(GenericList):
    html_template = template_base_path("list")
    titulo = "Clientes_sucursales"
    titulo_descripcion = "Sucursales Clientes"
    main_data_model = main_model
    model_name = "cat_d_clientessucursales"

    def get_data(self, pkcliente, search_value=''):
        data = self.main_data_model.objects.filter(IDCliente__pk=pkcliente)

        if '' == search_value:
            return list(
                data.all())
        else:
            return list(data.filter(
                Q(IDCliente__icontains=search_value) | Q(NombreContacto__icontains=search_value)))
    
    def get(self, request, pkcliente):
        search_value = ParametroUsuario.get_valor(
            request.user, 'basic_search', self.model_name)
        return self.base_render(
            request, self.get_data(pkcliente, search_value), search_value)

    def post(self, request, pkcliente):
        if "search" == request.POST.get('action', ''):
            search_value = request.POST.get('valor', '')
        else:
            search_value = ParametroUsuario.get_valor(
                request.user, 'basic_search', self.model_name)
        return self.base_render(
            request, self.get_data(pkcliente, search_value), search_value)


class Read(GenericRead):
    titulo_descripcion = "Clientes_sucursales"
    model_name = "cat_d_clientessucursales"
    base_data_form = base_form
    main_data_model = main_model


class Create(GenericCreate):
    titulo = "Clientes_sucursales"
    model_name = 'cat_d_clientessucursales'
    base_data_form = base_form


class Update(GenericUpdate):
    titulo = "Clientes_sucursales"
    model_name = "cat_d_clientessucursales"
    base_data_form = base_form
    main_data_model = main_model


class Delete(GenericDelete):
    model_name = "cat_d_clientessucursales"
    main_data_model = main_model