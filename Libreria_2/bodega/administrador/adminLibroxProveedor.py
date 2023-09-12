from django.contrib import admin

class AdminTbLibroxProveedor(admin.ModelAdmin):
    list_display = ('isbn', 'id_proveedor')
    list_filter = ('isbn', 'id_proveedor')
    search_fields = ('isbn', 'id_proveedor')  # Ajusta esto según tus modelos reales

    #readonly_fields = ('isbn', 'id_proveedor')
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('isbn', 'id_proveedor')
        }),
    )

    list_per_page = 10