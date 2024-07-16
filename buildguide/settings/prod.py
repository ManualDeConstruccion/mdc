from .base import *
import environ
import os

# Carga las variables de entorno desde .env
# we load the variables from the .env file to the environment
env = environ.Env()
environ.Env.read_env()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env("DB_NAME_PROD"),
        'USER': env("DB_USER_PROD"),
        'PASSWORD': env("DB_PASSWORD_PROD"),
        'HOST': env("DB_HOST_PROD"),
        'PORT': env("DB_PORT_PROD"),
    }
}

# Email Backend for development
# Use console backend for development. Emails will be printed to the console.
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '/staticfiles/'
STATICFILES_DIRS = [BASE_DIR.child('staticfiles')]

# Media files
# Defines the base URL and directory to serve user uploaded files during development
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')

# Logging configuration for development
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
