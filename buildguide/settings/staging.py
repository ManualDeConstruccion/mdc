from .base import *
import environ
import os

# Carga las variables de entorno desde .env
# we load the variables from the .env file to the environment
env = environ.Env()
environ.Env.read_env()

SECRET_KEY = env("DJANGO_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env("DB_NAME_DEV"),
        'USER': env("DB_USER_DEV"),
        'PASSWORD': env("DB_PASSWORD_DEV"),
        'HOST': env("DB_HOST_DEV"),
        'PORT': env("DB_PORT_DEV"),
    }
}

# Email Backend for development
# Use console backend for development. Emails will be printed to the console.
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'
DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
STATICFILES_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'

# Media files
# Defines the base URL and directory to serve user uploaded files during development
MEDIA_URL = '/media/'
MEDIA_ROOT = 'media/' 

GS_BUCKET_NAME = 'mdc-storage'

