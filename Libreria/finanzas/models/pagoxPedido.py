from django.db import models
from bodega.models.pedido import TbPedidos
from .pagos import TbPagos



# Create your models here.



class TbPagosxpedidos(models.Model):
    id_pago = models.OneToOneField(TbPagos, models.DO_NOTHING, db_column='id_pago', primary_key=True)  # The composite primary key (id_pago, id_pedido) found, that is not supported. The first column is selected.
    id_pedido = models.ForeignKey(TbPedidos, models.DO_NOTHING, db_column='id_pedido')

    class Meta:
        managed = True
        db_table = 'tb_pagosxpedidos'
        unique_together = (('id_pago', 'id_pedido'),)