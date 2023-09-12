from django.db import models
from Proyecto.bodega.models.pedido import TbPedidos
from Proyecto.bodega.models.proveedor import TbProveedor
from recursos_humanos.models.empleados import TbEmpleado

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

    def __str__(self):
        return str(self.id_factura_proveedor)

    class Meta:
        managed = True
        db_table = 'tb_factura_proveedor'
        verbose_name = 'Factura Proveedor'
        verbose_name_plural = 'Facturas Proveedor'