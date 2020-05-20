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

def template_base_path(file):
    return 'catalogos/cat_d_clientessucursales/' + file + ".html"

class List(GenericList):
    html_template = template_base_path("list")
    titulo = "Clientes_sucursales"
    titulo_descripcion = "Sucursales Clientes"
    main_data_model = main_model
    model_name = "cat_d_clientessucursales"

    def get_data(self, search_value=''):
        if '' == search_value:
            return list(
                self.main_data_model.objects.all())
        else:
            return list(self.main_data_model.objects.filter(
                Q(IDCliente__icontains=search_value) | Q(NombreContacto__icontains=search_value)))

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