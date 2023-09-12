from django.db import models
from .libro import *
from .categoria import TbCategoria

#import para pedidos
from recursos_humanos.models.empleados import TbEmpleado

# Create your models here.

class TbCategoriaxlibro(models.Model):
    id_libxcat = models.AutoField(primary_key=True)
    id_libro = models.ForeignKey(TbLibros, on_delete=models.CASCADE, db_column='id_libro') # The composite primary key (id_libro, id_categoria) found, that is not supported. The first column is selected.
    id_categoria = models.ForeignKey(TbCategoria, models.DO_NOTHING, db_column='id_categoria')

    def __str__(self):
        return f"{self.id_categoria} - {self.id_libro}"

    class Meta:
            managed = True
            db_table = 'tb_categoriaxlibro'
            verbose_name = 'Categoria-Libro'
            verbose_name_plural = 'Categorias-Libros'