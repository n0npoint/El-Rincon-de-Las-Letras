from django.db import models
from .proveedor import TbProveedor
from .editorial import TbEditorial



class TbEditorialxproveedor(models.Model):
    id_proveedor = models.OneToOneField(TbProveedor, models.DO_NOTHING, db_column='id_proveedor', primary_key=True)  # The composite primary key (id_proveedor, id_editorial) found, that is not supported. The first column is selected.
    id_editorial = models.ForeignKey(TbEditorial, models.DO_NOTHING, db_column='id_editorial')

    def __str__(self):
        return f"{self.id_proveedor} - {self.id_proveedor}"

    class Meta:
            managed = True
            db_table = 'tb_editorialxproveedor'
            verbose_name = 'Editorial-Proveedor'
            verbose_name_plural = 'Editorial-Proveedor'