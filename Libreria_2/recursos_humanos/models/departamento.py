from django.db import models

class TbDepartamento(models.Model):
    id_departamento = models.AutoField(primary_key=True, verbose_name='ID Departamento')
    nombre = models.CharField(max_length=20, verbose_name='Nombre Departamento')
    descripcion = models.CharField(max_length=200, blank=True, null=True, verbose_name='Descripción')

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'tb_departamento'
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'