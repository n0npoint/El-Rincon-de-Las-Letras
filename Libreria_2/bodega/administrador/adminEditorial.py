from django.contrib import admin

class AdminEditorial(admin.ModelAdmin):
    list_display = ('id_editorial', 'nombre', 'telefono', 'sitio_web')
    search_fields = ('id_editorial', 'nombre', 'telefono', 'sitio_web')
    list_filter = ('id_editorial', 'nombre', 'sitio_web')
    readonly_fields = ('id_editorial',) 

    
    fieldsets = (
        ('Información Básica', {
            'fields': ('id_editorial', 'nombre')
        }),
        ('Dirección y Ciudad', {
            'fields': ('direccion', 'ciudad')
        }),
        ('Contacto', {
            'fields': ('telefono', 'email', 'sitio_web')
        })
    )

    list_per_page = 10 
