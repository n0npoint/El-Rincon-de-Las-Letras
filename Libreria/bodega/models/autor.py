from django.db import models

class TbAutor(models.Model):
    id_autor = models.AutoField(primary_key=True , verbose_name='ID Autor')
    nombre = models.CharField(max_length=100 , verbose_name='Nombre')
    fecha_nacimiento = models.DateTimeField(blank=True, null=True , verbose_name='F. Nac')
    ciudad_origen = models.CharField(max_length=50, blank=True, null=True , verbose_name='C. Origen')
    nacionalidad = models.CharField(max_length=50, blank=True, null=True , verbose_name='Nacionalidad')

    def __str__(self):
        return self.nombre
    
    class Meta:
        managed = True
        db_table = 'tb_autor'
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'