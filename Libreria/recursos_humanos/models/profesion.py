from django.db import models



class TbProfesion(models.Model):
    id_cargo = models.AutoField(primary_key=True , verbose_name='ID Cargo')
    nombre_cargo = models.CharField(unique=True, max_length=45 , verbose_name='Nombre Profesion')
    descripcion = models.CharField(max_length=200, blank=True, null=True , verbose_name='Descripcion')

    def __str__(self):
        return self.nombre_cargo

    class Meta:
        db_table = 'tb_profesion'
        verbose_name = 'Profesion'
        verbose_name_plural = 'Profesiones'