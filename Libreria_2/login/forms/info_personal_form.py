from django import forms
from cliente.models.cliente import TbCliente


class ClienteForm(forms.ModelForm):
    
    class Meta():

        model = TbCliente
        fields = ["dni" , "nombre" , "apellido" , "direccion" , "numero_telefono" , 
                "email" , "foto"]

