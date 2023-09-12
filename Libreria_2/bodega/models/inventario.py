from django.db import models
from recursos_humanos.models.empleados import TbEmpleado
from .libro import TbLibros
from .pedido import TbPedidos
from ventas.models.devolucion import TbDevolucion

class TbInventario(models.Model):
    isbn = models.OneToOneField(TbLibros, on_delete=models.DO_NOTHING, db_column='isbn', primary_key=True)
    nombre = models.CharField(max_length=45)
    precio_compra = models.DecimalField(max_digits=10, decimal_places=2)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.IntegerField()
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    edicion = models.CharField(max_length=20)
    id_pedido = models.ForeignKey(TbPedidos, on_delete=models.DO_NOTHING, db_column='id_pedido')
    id_devolucion = models.ForeignKey(TbDevolucion, on_delete=models.DO_NOTHING, db_column='id_devolucion', blank=True, null=True)
    id_empleado = models.ForeignKey(TbEmpleado, on_delete=models.DO_NOTHING, db_column='id_empleado')
    fecha_registro = models.DateTimeField()

    def __str__(self):
        return self.nombre

    class Meta:
        managed = True
        db_table = 'tb_inventario'