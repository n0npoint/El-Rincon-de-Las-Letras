from django.db import models
from bodega.models.proveedor import TbProveedor
from bodega.models.pedido import TbPedidos
from recursos_humanos.models.empleados import TbEmpleado



# Create your models here.

class TbFacturaProveedor(models.Model):
    id_factura_proveedor = models.AutoField(primary_key=True)
    id_empleado = models.ForeignKey(TbEmpleado, models.DO_NOTHING, db_column='id_empleado')
    id_pedido = models.ForeignKey(TbPedidos, models.DO_NOTHING, db_column='id_pedido')
    id_proveedor = models.ForeignKey(TbProveedor, models.DO_NOTHING, db_column='id_proveedor')
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    impuesto = models.DecimalField(max_digits=10, decimal_places=2)
    descuento = models.DecimalField(max_digits=10, decimal_places=2)
    total_pagar = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_emision = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'tb_factura_proveedor'