from django.contrib import admin


# Register your models here.


class AdminEmpleado(admin.ModelAdmin):
    list_display = ('id_empleado' , 'nombre', 'username' , 'id_departamento' , 'id_cargo')
    search_fields = ('id_empleado', 'nombre' , 'id_departamento__nombre' , 'id_cargo__nombre_cargo')
    list_filter = ('id_cargo__nombre_cargo' , 'id_departamento__nombre')
    readonly_fields = ('id_empleado', 'fecha_contratacion')

    fieldsets = (
            (None, {
                'fields': ('id_empleado', 'dni', 'nombre', 'apellido', 'fecha_nacimiento')
            }),
            ('Contacto', {
                'fields': ('numero_telefono', 'numero_celular', 'email')
            }),
            ('Usuario', {
                'fields': ('username',)
            }),
            ('Departamento y Cargo', {
                'fields': ('id_departamento', 'id_cargo')
            }),
            ('Contratación y Foto', {
                'fields': ('fecha_contratacion', 'foto')
            }),
        )



