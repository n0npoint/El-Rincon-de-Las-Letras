from django.db import models
from .facturaCliente import TbFacturaCliente
from recursos_humanos.models.empleados import TbEmpleado
from cliente.models.cliente import TbCliente
from bodega.models.libro import TbLibros

class TbDevolucion(models.Model):
    id_devolucion = models.AutoField(primary_key=True)
    id_libro = models.ForeignKey(TbLibros, on_delete=models.DO_NOTHING, db_column='id_libro')
    id_factura = models.ForeignKey(TbFacturaCliente, on_delete=models.DO_NOTHING, db_column='id_factura')
    id_cliente = models.ForeignKey(TbCliente, on_delete=models.DO_NOTHING, db_column='id_cliente')
    id_empleado = models.ForeignKey(TbEmpleado, on_delete=models.DO_NOTHING, db_column='id_empleado')
    descripcion = models.CharField(max_length=200, blank=True, null=True)
    estado = models.CharField(max_length=20)
    fecha_devolucion = models.DateTimeField()

    def __str__(self):
        return f"{self.id_devolucion}"


    class Meta:
        managed = True
        db_table = 'tb_devolucion'
        unique_together = (('id_devolucion', 'id_libro'),)
        verbose_name = "Devolucion"
        verbose_name_plural = "Devoluciones"