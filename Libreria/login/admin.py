from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import *

class AdminHistorial(admin.ModelAdmin):
    list_display = ('cod_historial' , 'username' , 'fecha_hora_conexion' , 'fecha_hora_desconexion')
    search_fields = ['cod_historial', 'username__username']
    list_filter = ('fecha_hora_conexion' , )
    date_hierarchy = 'fecha_hora_conexion'


# Configuracion Para Administracion de Usuarios
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = TbUsuario

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = TbUsuario
        exclude = ['fecha_registro' , 'ultima_conexion']

class CustomUserAdmin(BaseUserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'rol', 'estado', 'avatar')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

admin.site.register(TbUsuario, CustomUserAdmin)
admin.site.register(TbHistorialActividad , AdminHistorial)


