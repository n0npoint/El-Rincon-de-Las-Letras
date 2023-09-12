
from django.db import models
from recursos_humanos.models.empleados import TbEmpleado
from django.conf import settings

class TbCliente(models.Model):
    id_cliente = models.AutoField(primary_key=True, verbose_name='ID Cliente')
    dni = models.CharField(unique=True, max_length=15)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    numero_telefono = models.CharField(max_length=20)
    username = models.OneToOneField(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='username', verbose_name='Username')
    email = models.CharField(unique=True, max_length=50)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    ultima_compra = models.DateTimeField(auto_now_add=True)
    monto_total_compra = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    registrado_por = models.ForeignKey(TbEmpleado, models.DO_NOTHING, db_column='registrado_por' , null=True)
    foto = models.ImageField(upload_to="clientes", default="clientes/clientes_empty.png", blank=True, null=True, verbose_name='Foto')

    def __str__(self):
        return str(self.id_cliente)
    
    class Meta:
        managed = True
        db_table = 'tb_cliente'
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'