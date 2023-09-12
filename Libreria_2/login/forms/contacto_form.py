from django import forms

class FormularioContacto(forms.Form):
    nombre = forms.CharField(label='Nombre' , max_length=10 , required=True)
    asunto = forms.CharField(label='Asunto' , max_length=20 , required=True)
    mensaje = forms.CharField(label='Mensaje' , max_length=1000 , widget=forms.Textarea , required=True)