from django.contrib import admin

class AdminTbProveedor(admin.ModelAdmin):
    list_display = ('id_proveedor', 'nombre', 'telefono', 'sitio_web')
    search_fields = ('id_proveedor', 'nombre', 'telefono', 'sitio_web')
    list_filter = ('id_proveedor', 'nombre', 'sitio_web')
    readonly_fields = ('id_proveedor',)

    fieldsets = (
        ('Información Básica', {
            'fields': ('id_proveedor', 'nombre')
        }),
        ('Dirección y Ciudad', {
            'fields': ('direccion', 'ciudad')
        }),
        ('Contacto', {
            'fields': ('telefono', 'email', 'sitio_web')
        }),
        ('Contrato', {
            'fields': ('inicio_contrato', 'fin_contrato')
        }),
        ('Descripción', {
            'fields': ('descripcion',)
        })
    )

    list_per_page = 10

