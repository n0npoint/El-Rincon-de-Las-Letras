from django.db import models
from .ventas import TbVentas
from bodega.models.libro import TbLibros

class TbLibrosxventas(models.Model):
    id_venta = models.OneToOneField(TbVentas, on_delete=models.DO_NOTHING, related_name='lixv_venta', db_column='id_venta', primary_key=True)
    id_libro = models.ForeignKey(TbLibros, on_delete=models.DO_NOTHING, related_name='lixv_libro', db_column='id_libro')
    cantidad = models.IntegerField()
    valor_individual = models.DecimalField(max_digits=10, decimal_places=2)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.id_venta}"


    class Meta:
        managed = True
        db_table = 'tb_librosxventas'
        unique_together = (('id_venta', 'id_libro'),)
        verbose_name = "Libro - Venta"
        verbose_name_plural = "Libros - Ventas"