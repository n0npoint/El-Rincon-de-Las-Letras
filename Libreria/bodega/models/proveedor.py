from django.db import models

#import para pedidos

# Create your models here.

class TbProveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True , verbose_name="ID Proveedor")
    nombre = models.CharField(max_length=50 , verbose_name="Nombre")
    direccion = models.CharField(max_length=200 , verbose_name="Direccion")
    ciudad = models.CharField(max_length=50 , verbose_name="Ciudad")
    telefono = models.CharField(unique=True, max_length=20 , verbose_name="Telefono")
    email = models.CharField(unique=True, max_length=50 , verbose_name="Email")
    sitio_web = models.CharField(unique=True, max_length=50 , verbose_name="Sitio Web")
    inicio_contrato = models.DateTimeField(verbose_name="Inicio Contrato")
    fin_contrato = models.DateTimeField(verbose_name="Fin Contrato")
    descripcion = models.CharField(max_length=200, blank=True, null=True , verbose_name="Descripcion")

    def __str__(self):
        return self.nombre

    class Meta:
            managed = True
            db_table = 'tb_proveedor'
            verbose_name = 'Proveedor'
            verbose_name_plural = 'Proveedores'

