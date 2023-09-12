from django.db import models
from recursos_humanos.models.empleados import TbEmpleado
from cliente.models.cliente import TbCliente


class TbFacturaCliente(models.Model):
    id_factura = models.AutoField(primary_key=True)
    id_empleado = models.ForeignKey(TbEmpleado, on_delete=models.DO_NOTHING, db_column='id_empleado')
    id_cliente = models.ForeignKey(TbCliente, on_delete=models.DO_NOTHING, db_column='id_cliente')
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    impuesto = models.DecimalField(max_digits=10, decimal_places=2)
    descuento = models.DecimalField(max_digits=10, decimal_places=2)
    total_compra = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pago = models.CharField(max_length=20)
    estado_pago = models.CharField(max_length=20)
    fecha_emision = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id_factura}"


    class Meta:
        managed = True
        db_table = 'tb_factura_cliente'
        verbose_name = "Factura Cliente"
        verbose_name_plural = "Facturas Cliente"