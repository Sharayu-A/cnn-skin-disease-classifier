import os
from pathlib import Path
from dotenv import load_dotenv
from google.oauth2 import service_account

# ==================================================
# BASIC
# ==================================================

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "dev-secret-key"

DEBUG = True

ALLOWED_HOSTS = ["*"]


# ==================================================
# APPS
# ==================================================

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'skin_disease_classifier',

    # REQUIRED for GCS
    'storages',
]


# ==================================================
# MIDDLEWARE
# ==================================================

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]


# ==================================================
# URLS / WSGI
# ==================================================

ROOT_URLCONF = 'CNN.urls'
WSGI_APPLICATION = 'CNN.wsgi.application'


# ==================================================
# TEMPLATES
# ==================================================

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "skin_disease_classifier/templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# ==================================================
# DATABASE (LOCAL POSTGRESQL)
# ==================================================

SECRET_KEY = os.getenv("SECRET_KEY", "dev")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv("DB_NAME", "cnn_db"),
        'USER': os.getenv("DB_USER", "postgres"),
        'PASSWORD': os.getenv("DB_PASSWORD", "root"),
        'HOST': os.getenv("DB_HOST", "localhost"),
        'PORT': '5432',
    }
}



# ==================================================
# STATIC FILES
# ==================================================

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "skin_disease_classifier/static"]


# ==================================================
# GOOGLE CLOUD STORAGE (DJANGO 5+ CORRECT WAY)
# ==================================================
# IMPORTANT:
# service-account.json must be beside manage.py
# NOT inside app folders

STORAGES = {
    "default": {
        "BACKEND": "storages.backends.gcloud.GoogleCloudStorage",
        "OPTIONS": {
            "bucket_name": "skin-diseases-gcs-bucket",
            # "credentials": service_account.Credentials.from_service_account_file(
            #     BASE_DIR / "service-account.json"
            # ),
        },
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}


# ==================================================
# DEFAULTS
# ==================================================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
