from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-local-secret-key-should-be-unique-and-secret'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '*']

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
# Adjust the database settings for your local development environment
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mdc',
        'USER': 'postgres',
        'PASSWORD': 'Subdere.2022',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static')]

# Media files
# Defines the base URL and directory to serve user uploaded files during development
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')

# Email Backend
# Configure a local email backend if necessary, for development purposes
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'