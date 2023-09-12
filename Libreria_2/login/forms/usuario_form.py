from django import forms
from django.contrib.auth.forms import UserCreationForm
from login.models import TbUsuario 
import re
 # Asegúrate de importar correctamente tu modelo

class UsuarioForm(UserCreationForm):
    class Meta:
        model = TbUsuario
        fields = ["username", "password1", "password2"]

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if not self.username_valido(username):
            raise forms.ValidationError("El nombre de usuario no cumple con los requisitos.")
        return username

    def username_valido(self, username):
        return bool(re.match(r'^[a-zA-Z0-9@]+$', username))