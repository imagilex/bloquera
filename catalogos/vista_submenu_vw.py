from django.shortcuts import render
from django.views import View


class SubMenu(View):
    """
    Vista disparada para momentos en que no se localiza un objeto en la
    base de datos para alguna de sus operaciones CRUD
    """

    def get(self, request):
        return render(request, "catalogos/vista_submenu/submenu.html", {
            'titulo': "Catalogos",
            'titulo_descripcion': '',
            'toolbar': False,
            'footer': False,
            'read_only': True,
            'alertas': [],
            'req_chart': False,
            'search_value': '',
            'forms': None,
        })