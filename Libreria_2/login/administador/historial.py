from django.contrib import admin


class AdminHistorial(admin.ModelAdmin):
    list_display = ('cod_historial' , 'username' , 'fecha_hora_conexion' , 'fecha_hora_desconexion')
    search_fields = ['cod_historial', 'username__username']
    list_filter = ('fecha_hora_conexion' , )
    date_hierarchy = 'fecha_hora_conexion'