from django.db import models

class TbEditorial(models.Model):
    id_editorial = models.AutoField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=50)
    direccion = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=50)
    telefono = models.CharField(unique=True, max_length=20)
    email = models.CharField(unique=True, max_length=50)
    sitio_web = models.CharField(unique=True, max_length=200)


    def __str__(self):
        return self.nombre

    class Meta:
            managed = True
            db_table = 'tb_Editorial'
            verbose_name = 'Editorial'
            verbose_name_plural = 'Editoriales'
