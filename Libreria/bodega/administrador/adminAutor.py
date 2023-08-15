from django.contrib import admin

class AdminAutor(admin.ModelAdmin):
    list_display = ('id_autor' , 'nombre' , 'nacionalidad')
    search_fields = ('id_autor', 'nombre')
    list_filter = ('id_autor' , 'nombre')

    readonly_fields = ('id_autor',)

    fieldsets = (
        ('General', {
            'fields': ('id_autor', 'nombre', 'nacionalidad', 'ciudad_origen', 'fecha_nacimiento')
        }),
    )
        