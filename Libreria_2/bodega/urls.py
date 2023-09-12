from django.urls import path

from .Views.libro_views import *
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('gestionlibro/', gestionlibro, name='gestionlibro'),
    path('gestionlibro/agregarlibro/', agregar_libro, name='agregarlibro'),
    path('eliminarlibro/<int:id_libro>/' , eliminarlibro , name='eliminarlibro'),
    path('gestionlibro/edicionlibro/<int:id_libro>/' , edicion_libro , name='edicionlibro'),
    path('existe_isbn/', existe_isbn, name='existe_isbn'),

    #path('<path:undefined_path>/', redirect_to_home, name='redirigir_a_pagina_principal'),







    path('formulario/', formulario, name='formulario'),

]
