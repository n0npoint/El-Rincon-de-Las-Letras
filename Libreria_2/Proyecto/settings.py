"""
Django settings for Proyecto project.

Generated by 'django-admin startproject' using Django 4.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-fjw5lshvjesr6itpmhxsaz%+j29$-d*(jphk!ktie+akl8+-&='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.humanize',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'crispy_bootstrap4',
    'cliente',
    'bodega',
    'finanzas',
    'login',
    'recursos_humanos',
    'ventas',
    'tienda',
    'carrito',

]




MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Proyecto.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'carrito.context_processors.importe_total_carro',
            ],
        },
    },
]

WSGI_APPLICATION = 'Proyecto.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'libreria',
        'USER': 'admin',
        'PASSWORD': '12345678',
        'HOST': 'localhost',  
        'PORT': '', 
        'OPTIONS': {
            'charset': 'utf8mb4',
            'sql_mode': 'traditional',  # Opcional, ajusta el modo SQL según tus necesidades.
        },
        'CONN_MAX_AGE': 600,
                  
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'es-ES'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


#Configuracion para la tabla usuario personalizada

AUTH_USER_MODEL = 'login.TbUsuario'

#Configuracion de jazzmin

JAZZMIN_SETTINGS = {

    "show_ui_builder": True,

    "copyright": "El Rincon de las Letras 2023",
    "site_logo": "\img\logos\logo.png",
    "welcome_sign": "El Rincon de las Letras - Panel de Administracion",
    "site_title": "El Rincon de las Letras",
    "site_brand": "Panel",
        "topmenu_links": [

        # external url that opens in a new window (Permissions can be added)
        {"name": "Sitio Web", "url": "http://127.0.0.1:8000/", "new_window": True},

        # model admin to link to (Permissions checked against model)
        {"model": "auth.User"},

        # App with dropdown menu to all its models pages (Permissions checked against models)
        {"app": "bodega"},
        {"app": "cliente"},
        {"app": "finanzas"},
        {"app": "recursos_humanos"},
        {"app": "ventas"},
    ],

        # Whether to display the side menu
    "show_sidebar": True,

    # Whether to aut expand the menu
    "navigation_expanded": False,


    # Custom links to append to app groups, keyed on app name
    "custom_links": {
        "books": [{
            "name": "Make Messages", 
            "url": "make_messages", 
            "icon": "fas fa-comments",
            "permissions": ["books.view_book"]
        }]
    },



    "icons": {
        "auth": "fas fa-users-cog",
        "bodega": "fas fa-box",
        "cliente": "fas fa-address-book",
        "finanzas": "fas fa-money-bill-wave",
        "recursos_humanos": "fas fa-user-tie",
        "ventas": "fas fa-cash-register",
        "login": "fas fa-user-alt",

        "auth.Group": "fas fa-users",
    },

    "default_icon_children": "fas fa-arrow-right",
    
}


#Configuracion para Crispy forms

CRISPY_ALLOWED_TEMPLATE_PACK ="bootstrap4"
CRISPY_TEMPLATE_PACK ="bootstrap4"


#Configuracion Envios de Email en Outlook

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.office365.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'soport3_rinconletras2023hn@outlook.com'
EMAIL_HOST_PASSWORD = 'ing_Sistema2'

