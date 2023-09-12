from django.db import models
from django.conf import settings
from .departamento import TbDepartamento
from .profesion import TbProfesion

class TbEmpleado(models.Model):
    id_empleado = models.AutoField(primary_key=True, verbose_name='ID Empleado')
    dni = models.CharField(unique=True, max_length=20, verbose_name='DNI')
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    apellido = models.CharField(max_length=50, verbose_name='Apellido')
    fecha_nacimiento = models.DateTimeField(verbose_name='Fecha Nacimiento')
    numero_telefono = models.CharField(unique=True, max_length=20, verbose_name='Número de Teléfono')
    numero_celular = models.CharField(unique=True, max_length=20, verbose_name='Número de Celular')
    email = models.CharField(unique=True, max_length=50, verbose_name='Email')
    username = models.OneToOneField(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='username', verbose_name='Username')
    id_departamento = models.ForeignKey(TbDepartamento, models.DO_NOTHING, db_column='id_departamento', verbose_name='ID Departamento')
    id_cargo = models.ForeignKey(TbProfesion, models.DO_NOTHING, db_column='id_cargo', verbose_name='ID Cargo')
    fecha_contratacion = models.DateTimeField(verbose_name='Fecha Contratación', auto_now_add=True)
    foto = models.ImageField(upload_to="empleados",  blank=True, null=True, verbose_name='Foto')


    def __str__(self):
       return str(self.id_empleado)

    class Meta:
        db_table = 'tb_empleado'
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'