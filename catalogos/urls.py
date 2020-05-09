from django.urls import include
from django.urls import path

urlpatterns = [
    path('materia_prima/', include('catalogos.cat_m_materiaprima_urls')),
]