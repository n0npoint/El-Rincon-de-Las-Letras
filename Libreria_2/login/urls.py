from django.urls import path
from .views import *
from .Views.miperfil_views import *

urlpatterns = [
    path('', inicio , name='portal'),
    path('nosotros/', nosotros, name='nosotros'),
    path('contacto/', contacto, name='contacto'),
    path('login/', iniciar_sesion, name='login'),
    path('miperfil/', miperfil, name='miperfil'),
    path('cerrar_sesion', cerrar_sesion, name='cerrar_sesion'),
    path('registrarse/', registrarse , name='registrarse'),
    path('registro_info_personal/<str:username>/', registro_info_personal , name='registro_info_personal'),
    path('mifactura/<int:id_factura>/', mifactura, name='mifactura'),



]
