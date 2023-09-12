from django.db import models



# Create your models here.
class TbServicios(models.Model):
    id_servicio = models.AutoField(primary_key=True)
    tipo_servicio = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.tipo_servicio


    class Meta:
        managed = True
        db_table = 'tb_servicios'
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"


    


