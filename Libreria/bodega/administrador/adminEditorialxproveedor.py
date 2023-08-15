from django.contrib import admin

class AdminEditorialxProveedor(admin.ModelAdmin):
    list_display = ('id_proveedor', 'id_editorial')
    list_filter = ('id_proveedor', 'id_editorial')
    search_fields = ('id_proveedor', 'id_editorial') 

    readonly_fields = ('id_proveedor', 'id_editorial')
    
    fieldsets = (
        ('Información General', {
            'fields': ('id_proveedor', 'id_editorial')
        }),
    )
