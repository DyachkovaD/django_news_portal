"""
Django settings for NewsPaper project.

Generated by 'django-admin startproject' using Django 4.2.14.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

import django.core.cache.backends.filebased
from dotenv import load_dotenv, find_dotenv
import os
import logging


# Build paths inside the project like this: BASE_DIR / 'subdir'.
load_dotenv(find_dotenv())

BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-3tk48s%_4k%qxxc29yuriiyi0tt^rj_l-%q1b+i12-9f3l7s=r'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

INSTALLED_APPS = [
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'news.apps.NewsConfig',
    'django_filters',
    'allauth',
    'protect',
    'sign',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.yandex',
    'django_apscheduler',
    'rest_framework',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',

    'news.middlewares.TimezoneMiddleware',
]

ROOT_URLCONF = 'NewsPaper.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'news.timezone_context.get_timezone',
            ],
        },
    },
]

WSGI_APPLICATION = 'NewsPaper.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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

# LANGUAGE_CODE = 'en-us'
LANGUAGES = [
    ('en-us', 'English'),
    ('ru', 'Русский'),
]

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale')
]

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

SITE_ID = 1

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'


ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_CONFIRMATION_REQUIRED = True
CSRF_COOKIE_DOMAIN = None

# ACCOUNT_FORMS = {'signup': 'news.forms.BasicSignupForm'}

#
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL')
EMAIL_USE_SSL = True

ADMINS = [
    # список всех админов в формате ('имя', 'их почта')
]
SERVER_EMAIL = os.getenv('DEFAULT_FROM_EMAIL')  # это будет у нас вместо аргумента FROM в массовой рассылке

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"
APSCHEDULER_RUN_NOW_TIMEOUT = 25  # Seconds

CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'cache_files')
    }
}
# DEBUG = False
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'style': '{',
#     'formatters': {
#         'debug': {'format': '%(levelname)s - %(asctime)s - %(message)s'},
#         'warning': {'format': '%(levelname)s - %(asctime)s - %(message)s - %(pathname)s'},
#         'error': {'format': '%(levelname)s - %(asctime)s - %(message)s - %(pathname)s - %(exc_info)s'},
#         'general': {'format': '%(levelname)s - %(asctime)s - %(module)s'},
#         'security': {'format': '%(levelname)s - %(asctime)s - %(module)s - %(message)s'},
#     },
#
#     'filters': {
#         'require_debug_true': {
#             '()': 'django.utils.log.RequireDebugTrue',
#         },
#         'require_debug_false': {
#             '()': 'django.utils.log.RequireDebugFalse',
#         },
#     },
#
#     'handlers': {
#         'console': {
#             'level': 'DEBUG',
#             'filters': ['require_debug_true'],
#             'class': 'logging.StreamHandler',
#             'formatter': 'debug',
#         },
#         'console_warning': {
#             'level': 'WARNING',
#             'filters': ['require_debug_true'],
#             'class': 'logging.StreamHandler',
#             'formatter': 'warning',
#         },
#         'console_error': {
#             'level': 'ERROR',
#             'filters': ['require_debug_true'],
#             'class': 'logging.StreamHandler',
#             'formatter': 'error',
#         },
#         'general': {
#             'class': 'logging.FileHandler',
#             'filters': ['require_debug_false'],
#             'filename': 'general.log',
#             'level': 'INFO',
#             'formatter': 'general',
#         },
#         'errors': {
#             'class': 'logging.FileHandler',
#             'filename': 'errors.log',
#             'level': 'ERROR',
#             'formatter': 'error',
#         },
#         'security': {
#             'class': 'logging.FileHandler',
#             'filename': 'security.log',
#             'level': 'INFO',
#             'formatter': 'security',
#         },
#         'mail_admins': {
#             'class': 'django.utils.log.AdminEmailHandler',
#             'level': 'ERROR',
#             'filters': ['require_debug_false'],
#             'formatter': 'warning',
#         },
#     },
#
#     'loggers': {
#         # '': {
#         #     'handlers': ['console'],
#         #     'level': 'DEBUG'
#         # },
#         'django': {
#             'handlers': ['console', 'console_warning', 'console_error', 'general'],
#             'level': 'DEBUG'
#         },
#         'django.security': {
#             'handlers': ['security'],
#             'propagate': True,
#         },
#         'django.request': {
#             'handlers': ['errors', 'mail_admins'],
#             'propagate': True,
#         },
#         'django.server': {
#             'handlers': ['errors', 'mail_admins'],
#             'propagate': True,
#         },
#         'django.template': {
#             'handlers': ['errors'],
#             'propagate': True,
#         },
#         'django.db.backends': {
#             'handlers': ['errors'],
#             'propagate': True,
#         },
#     },
# }
#
