from django.contrib import admin

# Register your models here.

class AdminProfesion(admin.ModelAdmin):
    list_display = ('id_cargo' , 'nombre_cargo')
    search_fields = ('id_cargo' , 'nombre_cargo')


