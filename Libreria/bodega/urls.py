from django.urls import path
from .views import home, redirect_to_home

urlpatterns = [
    path('', home, name='home'),
    path('<path:undefined_path>/', redirect_to_home, name='redirigir_a_pagina_principal'),
]
