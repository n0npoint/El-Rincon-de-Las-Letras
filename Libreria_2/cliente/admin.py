from django.contrib import admin

from .administrador.cliente import AdminCliente
from .models.cliente import TbCliente


# Register your models here.

admin.site.register(TbCliente, AdminCliente)