from django.contrib import admin

class AdminCategoria(admin.ModelAdmin):
    list_display = ('id_categoria' , 'nombre' , 'descripcion')
    search_fields = ('id_categoria', 'nombre')
    list_filter = ('id_categoria' , 'nombre')
    readonly_fields = ('id_categoria',)

    fieldsets = (
        ('General', {
            'fields': ('id_categoria', 'nombre', 'descripcion')
        }),
    )

    list_per_page = 10