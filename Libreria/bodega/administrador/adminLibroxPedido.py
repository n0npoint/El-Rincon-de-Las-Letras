from django.contrib import admin

class AdminTbLibroxPedido(admin.ModelAdmin):
    list_display = ('isbn', 'id_pedido', 'cantidad', 'subtotal', 'impuesto', 'descuento', 'total_pagar', 'fecha')
    list_filter = ('isbn', 'id_pedido')
    search_fields = ('isbn__titulo', 'id_pedido__id_pedido')  # Ajusta esto según tus modelos reales

    #readonly_fields = ('isbn', 'id_pedido')
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('isbn', 'id_pedido')
        }),
        ('Detalles del Pedido', {
            'fields': ('cantidad', 'subtotal', 'impuesto', 'descuento', 'total_pagar', 'fecha')
        }),
    )

