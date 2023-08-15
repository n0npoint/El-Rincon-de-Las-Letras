from django.contrib.auth.models import AbstractUser
from django.conf import settings

from django.db import models


class TbUsuario(AbstractUser):
    ROL_CHOICES = [
        ('cliente', 'Cliente'),
        ('bodega', 'Bodega'),
        ('finanzas', 'Finanzas'),
        ('rrhh', 'RRHH'),
        ('ventas', 'Ventas'),
        ('administrador', 'Administrador'),
    ]
    
    rol = models.CharField(max_length=20, choices=ROL_CHOICES, default='cliente')
    estado = models.CharField(max_length=20)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    ultima_conexion = models.DateTimeField(auto_now_add=True)
    avatar = models.ImageField(upload_to="user", default="user/user_empty.png", blank=True, null=True)

    class Meta:
        db_table = 'tb_usuarios'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

        




class TbHistorialActividad(models.Model):
    cod_historial = models.AutoField(primary_key=True , verbose_name='ID Historial')
    username = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, db_column='username' , verbose_name='Username')
    fecha_hora_conexion = models.DateTimeField(verbose_name='Fecha-Hora Conexion')
    fecha_hora_desconexion = models.DateTimeField(verbose_name='Fecha-Hora Desconexion')
    tiempo_conexion = models.DecimalField(max_digits=10, decimal_places=2 , verbose_name='Tiempo Online')

    class Meta:
        db_table = 'tb_historial_actividad'
        verbose_name = 'Historial de Actividad'
        verbose_name_plural = 'Historial de Actividad'