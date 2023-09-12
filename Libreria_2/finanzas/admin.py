from django.contrib import admin
from .models.servicios import TbServicios
from .models.salarios import TbSalarios
from .models.pagoxPedido import TbPagosxpedidos
from .models.pagos import TbPagos
from .models.facturaProveedor import TbFacturaProveedor

# Register your models here.


admin.site.register(TbPagos)
admin.site.register(TbFacturaProveedor)
admin.site.register(TbPagosxpedidos)
admin.site.register(TbSalarios)
admin.site.register(TbServicios)
