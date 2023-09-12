from django.db import models
from .libro import TbLibros
from .proveedor import TbProveedor



class TbLibroxproveedor(models.Model):
    isbn = models.OneToOneField(TbLibros, models.DO_NOTHING, db_column='isbn', primary_key=True)  # The composite primary key (isbn, id_proveedor) found, that is not supported. The first column is selected.
    id_proveedor = models.ForeignKey(TbProveedor, models.DO_NOTHING, db_column='id_proveedor')

    def __str__(self):
        return str(self.isbn)

    class Meta:
        managed = True
        db_table = 'tb_libroxproveedor'
        unique_together = (('isbn', 'id_proveedor'),)

        verbose_name = 'Libro-Proveedor'
        verbose_name_plural = 'Libro-Proveedor'