from django.db import models
from recursos_humanos.models.empleados import TbEmpleado
from .proveedor import TbProveedor
# Create your models here.



class TbPedidos(models.Model):

    TRANSACCION_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('aprobada', 'Aprobada'),
        ('rechazada', 'Rechazada'),
        ('Cancelada', 'Cancelada'),
        ('procesando', 'Procesando'),
        ('completada', 'Completada'),
    ]

    FORMA_PAGO_CHOICES = [
        ('efectivo', 'Efectivo'),
        ('tarjeta', 'Tarjeta de Crédito'),
        ('transferencia', 'Transferencia'),
        ('paypal', 'PayPal'),
    ]

    id_pedido = models.AutoField(primary_key=True)
    id_empleado = models.ForeignKey(TbEmpleado, models.DO_NOTHING, db_column='id_empleado', null=True)
    id_proveedor = models.ForeignKey(TbProveedor, models.DO_NOTHING, db_column='id_proveedor', null=True)
    id_factura_proveedor = models.IntegerField()
    fecha_solicitado = models.DateTimeField()
    estado = models.CharField(max_length=20 , choices=TRANSACCION_CHOICES , default='Pendiente')
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    impuesto = models.DecimalField(max_digits=10, decimal_places=2)
    descuento = models.DecimalField(max_digits=10, decimal_places=2)
    total_pagar = models.DecimalField(max_digits=10, decimal_places=2)
    forma_pago = models.CharField(max_length=20 , choices=FORMA_PAGO_CHOICES , default='Efectivo' )

    def __str__(self):
        return str(self.id_pedido)

    class Meta:
        managed = True
        db_table = 'tb_pedidos'
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'




