from .base import *
import environ
import os
import json
from google.cloud import secretmanager_v1 as secretmanager
from google.oauth2 import service_account
from storages.backends.gcloud import GoogleCloudStorage

# Carga las variables de entorno desde .env
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")
DEBUG = True
ALLOWED_HOSTS = ['*']

# Database Configuration
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
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Static files Configuration
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    # Agrega otros directorios de estáticos aquí si los tienes
]
STATIC_URL = 'https://storage.googleapis.com/mdc-storage/'
DEFAULT_FILE_STORAGE = os.environ.get("DEFAULT_FILE_STORAGE")
STATICFILES_STORAGE = os.environ.get("STATICFILES_STORAGE")
MEDIA_URL = '/media/'
MEDIA_ROOT = 'media/'

# Google Cloud Storage Configuration
def get_gcs_credentials():
    try:
        client = secretmanager.SecretManagerServiceClient()
        name = f"projects/manualdeconstruccion/secrets/compute_engine_credentials/versions/latest"
        response = client.access_secret_version(request={"name": name})
        return json.loads(response.payload.data.decode("UTF-8"))
    except Exception as e:
        print(f"Error loading GCS credentials: {e}")
        return None

GOOGLE_CLOUD_CREDENTIALS = get_gcs_credentials()
GS_CREDENTIALS = service_account.Credentials.from_service_account_info(GOOGLE_CLOUD_CREDENTIALS) if GOOGLE_CLOUD_CREDENTIALS else None

GS_BUCKET_NAME = os.environ.get("GS_BUCKET_NAME")
if GS_BUCKET_NAME and 'google.cloud.storage' in DEFAULT_FILE_STORAGE:
    gcs_storage = GoogleCloudStorage(credentials=GS_CREDENTIALS, bucket_name=GS_BUCKET_NAME)
    STATICFILES_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
    DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
    GS_DEFAULT_ACL = 'publicRead'
