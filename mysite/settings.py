"""
Django settings for mysite project.

Generated as part of the Django Girls Tutorial.
https://tutorial.djangogirls.org/en/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
# NOTE: Django normally auto-generates a random key here when you run
# `django-admin startproject`. Replace this with your own generated key
# (see the "Django installation" chapter) before you push this to GitHub.
SECRET_KEY = 'django-insecure-REPLACE-ME-WITH-YOUR-OWN-GENERATED-SECRET-KEY'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Django Girls Tutorial - "Django URLs" / "Deploy!" chapters:
# Once DEBUG is True and ALLOWED_HOSTS is empty, Django only allows
# localhost/127.0.0.1. We add the PythonAnywhere domain so the site
# will work once deployed.
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '.pythonanywhere.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Django Girls Tutorial - "Django models" chapter: register our blog app
    'blog',
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

ROOT_URLCONF = 'mysite.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

# Django Girls Tutorial - "Your first Django project!" chapter:
# Change LANGUAGE_CODE and TIME_ZONE to match where you live.
# Example: TIME_ZONE = 'America/Chicago' for Indiana (most of Indiana
# uses America/Indiana/Indianapolis).
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Indiana/Indianapolis'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'
# Django Girls Tutorial - "Your first Django project!" chapter: needed for
# deployment so `collectstatic` knows where to gather static files.
STATIC_ROOT = BASE_DIR / 'static'

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/models/fields/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
