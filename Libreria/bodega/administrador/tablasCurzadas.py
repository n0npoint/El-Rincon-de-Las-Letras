from django.contrib import admin

class AdminCategoriaxLibros(admin.ModelAdmin):
    list_display = ('id_libro' , 'id_categoria')
    search_fields = ('id_libro' , 'id_categoria')
    list_filter = ('id_libro' , 'id_categoria')

    readonly_fields = ('id_libro' , 'id_categoria')

    fieldsets = (
        ('General', {
            'fields': ('id_libro' , 'id_categoria')
        }),
    )
        