"""
URL configuration for Proyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from .Views.lista_compra.lista_compra import realizar_ventas

from .Views.vendedores.vendedores_views import ventas_mensuales_empleado 
from .Views.vendedores.vendedores_views import *
from .Views.facturas.factura_vista import *



urlpatterns = [
    path('gestion_ventas', gestion_ventas, name='gestion_ventas'),  #Menu Para administrar depto. de Ventas
    path('gestion_ventas/ventas_empleado/<int:id_empleado>/', ventas_mensuales_empleado, name='ventas_empleado_mes'),
    path('gestion_ventas/ventas_diarias/', ventas_diarias_mes_actual, name='ventas_diarias_mes'),
    path('gestion_ventas/ventas_libros_mensuales', ventas_libros_mensuales, name='ventas_libros_mensuales'),
    path('gestion_ventas/comparativa_ventas', ventas_empleados_anio_actual, name='comparativa_ventas'),
    path('gestion_ventas/comparativa_tipo_ventas', comparativa_tipo_ventas, name='comparativa_tipo_ventas'),

    path('factura/', factura_vista, name='factura_vista'),
    path('generar_factura/', factura_imprimir, name='generar_factura'),
    path('realizar_venta/', realizar_ventas, name='realizar_venta'),



]
