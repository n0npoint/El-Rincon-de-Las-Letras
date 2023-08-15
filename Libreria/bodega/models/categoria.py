from django.db import models

class TbCategoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        managed = True
        db_table = 'tb_categoria'
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
