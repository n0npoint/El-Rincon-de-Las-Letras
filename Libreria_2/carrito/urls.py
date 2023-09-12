from django.urls import path

from .views.carro_views import *


app_name = "carro"

urlpatterns = [
    path('', carrito, name='carrito'),
    path('agregar/<int:id_libro>', agregar_producto, name='agregar_producto'),
    path('eliminar/<int:id_libro>', eliminar_producto, name='eliminar_producto'),
    path('limpiar/', limpiar_carro, name='limpiar'),
    path('agregar/', carrito, name='agregar'),
    
    
    ]