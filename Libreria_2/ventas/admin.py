from django.contrib import admin
from .models.devolucion import TbDevolucion
from .models.librosxventas import TbLibrosxventas

from .models.ventas import TbVentas

from .models.facturaCliente import TbFacturaCliente

# Register your models here.


admin.site.register(TbFacturaCliente)
admin.site.register(TbDevolucion)
admin.site.register(TbLibrosxventas)
admin.site.register(TbVentas)