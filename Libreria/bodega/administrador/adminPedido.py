from django.contrib import admin

class AdminPedido(admin.ModelAdmin):
    list_display = ('id_pedido' , 'id_empleado' , 'id_proveedor' , 'id_factura_proveedor' , 
                    'fecha_solicitado' , 'total_pagar')
    search_fields = ('id_pedido' , 'id_empleado' , 'id_proveedor' , 'id_factura_proveedor' , 
                    'fecha_solicitado' , 'total_pagar')
    list_filter = ('id_pedido' , 'id_empleado' , 'id_proveedor' , 'fecha_solicitado')
    readonly_fields = ('id_pedido',)

    fieldsets = (
        ('Información Básica', {
            'fields': ('id_pedido', 'id_empleado', 'id_proveedor', 'id_factura_proveedor')
        }),
        ('Fechas y Estado', {
            'fields': ('fecha_solicitado', 'estado')
        }),
        ('Detalles de Pago', {
            'fields': ('subtotal', 'impuesto', 'descuento', 'total_pagar', 'forma_pago')
        })
    )
    

