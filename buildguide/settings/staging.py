from .base import *
import environ
import os

# Carga las variables de entorno desde .env
# we load the variables from the .env file to the environment

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get("DB_NAME_DEV"),
        'USER': os.environ.get("DB_USER_DEV"),
        'PASSWORD': os.environ.get("DB_PASSWORD_DEV"),
        'HOST': os.environ.get("DB_HOST_DEV"),
        'PORT': os.environ.get("DB_PORT_DEV"),
    }
}

# Email Backend for development
# Use console backend for development. Emails will be printed to the console.
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'
DEFAULT_FILE_STORAGE = os.environ.get("DEFAULT_FILE_STORAGE")
STATICFILES_STORAGE = os.environ.get("STATICFILES_STORAGE")
# Media files
# Defines the base URL and directory to serve user uploaded files during development
MEDIA_URL = '/media/'
MEDIA_ROOT = 'media/' 

GS_BUCKET_NAME = os.environ.get("GS_BUCKET_NAME")

