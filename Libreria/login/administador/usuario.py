from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# Configuracion Para Administracion de Usuarios
from login.models import TbUsuario


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