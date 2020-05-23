from django.shortcuts import render
from django.views import View

from .cat_m_empleado_forms import frmCat_M_Empleado as base_form
from .models import Cat_M_Empleado as main_model

from zend_django.views import GenericCreate
from zend_django.views import GenericDelete
from zend_django.views import GenericList
from zend_django.views import GenericRead
from zend_django.views import GenericUpdate
