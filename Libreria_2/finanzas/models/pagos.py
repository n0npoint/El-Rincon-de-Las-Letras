from django.db import models
from recursos_humanos.models.empleados import TbEmpleado
from .servicios import TbServicios
from .facturaProveedor import TbFacturaProveedor



# Create your models here.

class TbPagos(models.Model):
    id_pagos = models.AutoField(primary_key=True)
    id_servicio = models.ForeignKey(TbServicios, models.DO_NOTHING, db_column='id_servicio', blank=True, null=True)
    id_factura_proveedor = models.ForeignKey(TbFacturaProveedor, models.DO_NOTHING, db_column='id_factura_proveedor', blank=True, null=True)
    fecha_pago = models.DateTimeField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    forma_pago = models.CharField(max_length=20)
    estado_pago = models.CharField(max_length=20)
    id_empleado = models.ForeignKey(TbEmpleado, models.DO_NOTHING, db_column='id_empleado')

    def __str__(self):
        return f"{self.id_pagos}"


    class Meta:
        managed = True
        db_table = 'tb_pagos'
        verbose_name = "Pago"
        verbose_name_plural = "Pagos"