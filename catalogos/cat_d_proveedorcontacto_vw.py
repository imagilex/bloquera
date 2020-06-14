from django.shortcuts import render
from django.views import View

from .cat_d_proveedorcontacto_forms import frmCat_D_ProveedorContacto as base_form
from .models import Cat_D_ProveedorContacto as main_model

from zend_django.views import GenericCreate
from zend_django.views import GenericDelete
from zend_django.views import GenericList
from zend_django.views import GenericRead
from zend_django.views import GenericUpdate

from zend_django.parametros_models import ParametroUsuario
from django.db.models import Q

from django.http import HttpResponseRedirect
from django.urls import reverse

from zend_django.templatetags.op_helpers import crud_smart_button


def template_base_path(file):
    return 'catalogos/cat_d_proveedorcontacto/' + file + ".html"

class List(GenericList):
    html_template = template_base_path("list")
    titulo = "Contactos del Proveedor"
    titulo_descripcion = "Catalogo"
    main_data_model = main_model
    model_name = "cat_d_proveedorcontacto"

    def get_data(self, pkproveedor, search_value=''):
        data = self.main_data_model.objects.filter(IDProveedor__pk=pkproveedor)
        
        if '' == search_value:
            return list(
                data.all())
        else:
            return list(self.data.filter(
                Q(IDProveedor__icontains=search_value) | Q(NombreContacto__icontains=search_value)))

    def get(self, request, pkproveedor):
            search_value = ParametroUsuario.get_valor(
                request.user, 'basic_search', self.model_name)
            return self.base_render(
                request, self.get_data(pkproveedor, search_value), search_value)

    def post(self, request, pkproveedor):
        if "search" == request.POST.get('action', ''):
            search_value = request.POST.get('valor', '')
        else:
            search_value = ParametroUsuario.get_valor(
                request.user, 'basic_search', self.model_name)
        return self.base_render(
            request, self.get_data(pkproveedor, search_value), search_value)

class Read(GenericRead):
    titulo_descripcion = "Contactos del Proveedor"
    model_name = "cat_d_proveedorcontacto"
    base_data_form = base_form
    main_data_model = main_model

    def get(self, request, pk):
        if not self.main_data_model.objects.filter(pk=pk).exists():
            return HttpResponseRedirect(reverse('item_no_encontrado'))
        obj = self.main_data_model.objects.get(pk=pk)
        form = self.base_data_form(instance=obj)
        toolbar = []

        if request.user.has_perm(
                f"catalogos.view_cat_d_proveedorcontacto"):
            toolbar.append({
                'type': 'rlink',
                'url': reverse('cat_d_proveedorcontacto_list',kwargs={'pkproveedor':obj.IDProveedor.pk}),
                'label': crud_smart_button('list')})
        if request.user.has_perm(
                f"catalogos.change_cat_d_proveedorcontacto"):
            toolbar.append({
                'type': 'link_pk',
                'view': f'cat_d_proveedorcontacto_update',
                'pk': pk,
                'label': crud_smart_button('update')})
        if request.user.has_perm(
                f"catalogos.delete_cat_d_proveedorcontacto"):
            toolbar.append({
                'type': 'link_pk_del',
                'view': f'cat_d_proveedorcontacto_delete',
                'pk': pk,
                'label': crud_smart_button('delete')})
        return render(request, self.html_template, {
            'titulo': obj,
            'titulo_descripcion': self.titulo_descripcion,
            'toolbar': toolbar,
            'footer': False,
            'read_only': True,
            'alertas': [],
            'req_chart': False,
            'search_value': '',
            'forms': {'top': [{'form': form}]}
        })



class Create(GenericCreate):
    titulo = "Contactos del Proveedor"
    model_name = 'cat_d_proveedorcontacto'
    base_data_form = base_form


class Update(GenericUpdate):
    titulo = "Contactos del Proveedor"
    model_name = "cat_d_proveedorcontacto"
    base_data_form = base_form
    main_data_model = main_model


class Delete(GenericDelete):
    model_name = "cat_d_proveedorcontacto"
    main_data_model = main_model

    def get(self, request, pk):
        if not self.main_data_model.objects.filter(pk=pk).exists():
            return HttpResponseRedirect(reverse('item_no_encontrado'))
        obj = self.main_data_model.objects.get(pk=pk)
        try:
            obj.delete()
            return HttpResponseRedirect(reverse('cat_d_proveedorcontacto_list',kwargs={'pkproveedor':obj.IDProveedor.pk}))
        except ProtectedError:
            return HttpResponseRedirect(reverse('item_con_relaciones'))
        except IntegrityError:
            return HttpResponseRedirect(reverse('item_con_relaciones'))
