from django.db import models
from .autor import TbAutor
from .editorial import TbEditorial


class TbLibros(models.Model):
    DISPONIBILIDAD_OPCIONES = [
        ('disponible', 'Disponible'),
        ('no_disponible', 'No Disponible'),
    ]

    id_libro = models.AutoField(primary_key=True , verbose_name='ID Libro') 
    isbn = models.IntegerField(verbose_name='ISBN')
    titulo = models.CharField(max_length=100 , verbose_name='Titulo')
    id_autor = models.ForeignKey(TbAutor, models.DO_NOTHING, db_column='id_autor' , verbose_name='ID Autor')
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2 , verbose_name='Precio')
    sipnosis = models.CharField(max_length=200, blank=True, null=True , verbose_name='Sipnosis')
    disponibilidad = models.CharField(max_length=20, choices=DISPONIBILIDAD_OPCIONES , verbose_name='Disponibilidad')
    edicion = models.CharField(max_length=50, blank=True, null=True , verbose_name='Edicion')
    id_editorial = models.ForeignKey(TbEditorial, models.DO_NOTHING, db_column='id_editorial' , verbose_name='ID Editorial')
    caratula = models.ImageField(upload_to="libros", blank=True, null=True, verbose_name='Portada')
    
    def __str__(self):
        return self.titulo

    class Meta:
        managed = True
        db_table = 'tb_libros'
        unique_together = (('id_libro', 'isbn'),)
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
