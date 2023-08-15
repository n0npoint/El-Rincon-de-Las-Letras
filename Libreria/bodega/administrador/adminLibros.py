from django.contrib import admin

class AdminLibro(admin.ModelAdmin):
    list_display = ('id_libro' , 'titulo' , 'id_autor' , 'precio_venta')
    search_fields = ('id_libro' , 'titulo' , 'id_autor' , 'precio_venta')
    list_filter = ('id_libro' , 'titulo' , 'id_autor')
    readonly_fields = ('id_libro',)


    fieldsets = (
        ('Información Básica', {
            'fields': ('id_libro', 'isbn', 'titulo')
        }),
        ('Autor y Editorial', {
            'fields': ('id_autor', 'id_editorial')
        }),
        ('Detalles de Publicación', {
            'fields': ('precio_venta', 'disponibilidad', 'edicion')
        }),
        ('Contenido y Portada', {
            'fields': ('sipnosis', 'caratula')
        }),
    )