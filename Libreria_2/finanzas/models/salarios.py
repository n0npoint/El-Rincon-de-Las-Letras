from django.db import models
from recursos_humanos.models.empleados import TbEmpleado

# Create your models here.

class TbSalarios(models.Model):
    id_salario = models.AutoField(primary_key=True)
    id_empleado = models.ForeignKey(TbEmpleado, models.DO_NOTHING, db_column='id_empleado')
    salario_inicial = models.DecimalField(max_digits=10, decimal_places=2)
    salario_actual = models.DecimalField(max_digits=10, decimal_places=2)
    ihss = models.DecimalField(max_digits=10, decimal_places=2)
    rap = models.DecimalField(max_digits=10, decimal_places=2)
    infop = models.DecimalField(max_digits=10, decimal_places=2)
    salario_neto = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.id_salario}"


    class Meta:
        managed = True
        db_table = 'tb_salarios'
        verbose_name = "Salario"
        verbose_name_plural = "Salarios"