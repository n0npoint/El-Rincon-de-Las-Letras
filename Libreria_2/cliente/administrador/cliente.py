from django.contrib import admin

class AdminCliente(admin.ModelAdmin):
    list_display = ('id_cliente' , 'nombre', 'apellido' )
    search_fields = ('id_cliente', 'nombre' , 'apellido')
    list_filter = ('id_cliente' , 'nombre' , 'apellido')