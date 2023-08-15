from django.contrib import admin


#Configuracion del modelo departamentos en el panel de administracion

class AdminDepartamento(admin.ModelAdmin):
    list_display = ('id_departamento' , 'nombre')
    search_fields = ('id_departamento' , 'nombre')




