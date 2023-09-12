from django.contrib import admin

class AdminCategoriaxLibros(admin.ModelAdmin):
    list_display = ('id_libxcat','id_libro' , 'id_categoria')
    search_fields = ('id_libxcat','id_libro'  , 'id_categoria')
    list_filter = ('id_libxcat' ,'id_libro' , 'id_categoria')

    #readonly_fields = ('id_libxcat' , 'id_libro' , 'id_categoria')

    fieldsets = (
        ('General', {
            'fields': ('id_libro' , 'id_categoria')
        }),
    )
    
    list_per_page = 3