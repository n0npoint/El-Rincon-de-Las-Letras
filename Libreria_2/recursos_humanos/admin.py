from django.contrib import admin
from .administrador.departamentos import AdminDepartamento
from .administrador.empleados import AdminEmpleado
from .administrador.profesion import AdminProfesion
from .models.departamento import TbDepartamento
from .models.empleados import TbEmpleado
from .models.profesion import TbProfesion



#Registro del modelo del Area de Recursos Humanos
admin.site.register(TbDepartamento , AdminDepartamento)
admin.site.register(TbEmpleado , AdminEmpleado)
admin.site.register(TbProfesion , AdminProfesion)