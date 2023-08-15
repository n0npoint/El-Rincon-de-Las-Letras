from django.db import models



# Create your models here.
class TbServicios(models.Model):
    id_servicio = models.AutoField(primary_key=True)
    tipo_servicio = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tb_servicios'