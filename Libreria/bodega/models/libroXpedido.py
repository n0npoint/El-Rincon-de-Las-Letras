from django.db import models
from .libro import TbLibros
from .pedido import TbPedidos


class TbLibroxpedido(models.Model):
    isbn = models.OneToOneField(TbLibros, models.DO_NOTHING, db_column='isbn', primary_key=True)  # The composite primary key (isbn, id_pedido) found, that is not supported. The first column is selected.
    id_pedido = models.ForeignKey(TbPedidos, models.DO_NOTHING, db_column='id_pedido')
    cantidad = models.IntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    impuesto = models.DecimalField(max_digits=10, decimal_places=2)
    descuento = models.DecimalField(max_digits=10, decimal_places=2)
    total_pagar = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField()

    def __str__(self):
        return f"{self.isbn} - {self.id_pedido}"

    class Meta:
        db_table = 'tb_libroxpedido'
        unique_together = (('isbn', 'id_pedido'),)
        verbose_name = 'Libro-Pedido'
        verbose_name_plural = 'Libro-Pedido'