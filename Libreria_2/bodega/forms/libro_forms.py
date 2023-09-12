from django import forms
from bodega.models.libro import TbLibros


class LibroForm(forms.ModelForm):
    
    class Meta():

        model = TbLibros
        fields = ["isbn" , "titulo" , "id_autor" , "precio_venta" , "sipnosis" , 
                "disponibilidad" , "edicion" , "id_editorial" , "caratula"]

