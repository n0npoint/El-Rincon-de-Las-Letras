from django.db import models
from recursos_humanos.models.empleados import TbEmpleado
from .facturaCliente import TbFacturaCliente




class TbVentas(models.Model):
    id_venta = models.AutoField(primary_key=True)
    id_empleado = models.ForeignKey(TbEmpleado, on_delete=models.DO_NOTHING, db_column='id_empleado')
    id_factura = models.ForeignKey(TbFacturaCliente, on_delete=models.DO_NOTHING, db_column='id_factura')
    forma_pago = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    fecha_de_registro = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'tb_ventas'

