from django.shortcuts import redirect, render
from django.contrib import messages

def custom_login_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return view_func(request, *args, **kwargs)
        else:
            messages.error(request, "Debes iniciar sesión para acceder a esta página.")
            return redirect('login')
    return wrapper