from django.urls import path
from .views import *

urlpatterns = [
    path('catalogo/', catalogo , name='catalogo'),
    path('ver_item/<int:id_libro>/', verItem, name='ver_item'),
]