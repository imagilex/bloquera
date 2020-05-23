from django.shortcuts import render
from django.views import View

from .cat_d_proveedorcontacto_forms import frmCat_D_ProveedorContacto as base_form
from .models import Cat_D_ProveedorContacto as main_model

from zend_django.views import GenericCreate
from zend_django.views import GenericDelete
from zend_django.views import GenericList
from zend_django.views import GenericRead
from zend_django.views import GenericUpdate

def template_base_path(file):
    return 'catalogos/cat_d_proveedorcontacto/' + file + ".html"

class List(GenericList):
    html_template = template_base_path("list")
    titulo = "Proveedores_contactos"
    titulo_descripcion = "Catalogo"
    main_data_model = main_model
    model_name = "cat_d_proveedorcontacto"

    def get_data(self, search_value=''):
        if '' == search_value:
            return list(
                self.main_data_model.objects.all())
        else:
            return list(self.main_data_model.objects.filter(
                Q(IDProveedor__icontains=search_value) | Q(NombreContacto__icontains=search_value)))

class Read(GenericRead):
    titulo_descripcion = "Proveedores_contactos"
    model_name = "cat_d_proveedorcontacto"
    base_data_form = base_form
    main_data_model = main_model


class Create(GenericCreate):
    titulo = "Proveedores_contactos"
    model_name = 'cat_d_proveedorcontacto'
    base_data_form = base_form


class Update(GenericUpdate):
    titulo = "Proveedores_contactos"
    model_name = "cat_d_proveedorcontacto"
    base_data_form = base_form
    main_data_model = main_model


class Delete(GenericDelete):
    model_name = "cat_d_proveedorcontacto"
    main_data_model = main_model