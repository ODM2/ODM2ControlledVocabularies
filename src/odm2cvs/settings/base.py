"""
Django settings for djangoProject project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/

To setup the settings json file:
    1. rename settings_template.json to settings.json
    2. then write all the necessary data in it
    3. ???
    4. Profit!
"""

import sys
import json
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
from typing import Dict, Any, TextIO, List, Tuple, Union

BASE_DIR: Path = Path(__file__).resolve().parent.parent


config: Dict[str, Any] = {}

try:
    data_file: TextIO
    with open(BASE_DIR / 'settings' / 'settings.json') as data_file:
        config = json.load(data_file)
except IOError as ioe:
    sys.exit('You need to setup the settings data file (see instructions in base.py file.)')


try:
    SECRET_KEY: str = config['secret_key']
except KeyError:
    print()
    exit('The secret key is required in the settings.json file.')

ALLOWED_HOSTS: List[str] = []


# Application definition

INSTALLED_APPS: List[str] = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cvservices',
    'cvinterface',
]

MIDDLEWARE: List[str] = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'odm2cvs.urls'

TEMPLATES: List[Dict[str, Any]] = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR.parent / 'cvinterface' / 'templates']
        ,
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

WSGI_APPLICATION: str = 'odm2cvs.wsgi.application'


# Databases
DATABASES: Dict[str, Dict[str, Any]] = {}
for database in config['databases']:
    DATABASES[database['name']] = {
        'ENGINE': database['engine'],
        'NAME': database['schema'],
        'USER': database['user'] if 'user' in database else '',
        'PASSWORD': database['password'] if 'password' in database else '',
        'HOST': database['host'] if 'host' in database else '',
        'PORT': database['port'] if 'port' in database else '',
        'OPTIONS': database['options'] if 'options' in database else {}
    }

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS: List[Dict[str, str]] = [
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

LANGUAGE_CODE: str = 'en-us'

TIME_ZONE: str = 'UTC'

USE_I18N: bool = True

USE_L10N: bool = True

USE_TZ: bool = True

SITE_ID: int = 1

static_config: Dict = config['static'] if 'static' in config else {}
STATIC_ROOT: str = static_config['root'] if 'root' in static_config else ''
STATIC_URL: str = static_config['url'] if 'url' in static_config else ''

email_config: Dict = config['email'] if 'email' in config else {}
EMAIL_HOST: str = email_config['host'] if 'host' in email_config else ''
EMAIL_SENDER: str = email_config['sender'] if 'sender' in email_config else ''
EMAIL_RECIPIENTS: List[str] = email_config['recipients'] if 'recipients' in email_config else ''
EMAIL_BACKEND: str = 'django.core.mail.backends.smtp.EmailBackend'

recaptcha_config: Dict = config['recaptcha'] if 'recaptcha' in config else {}
RECAPTCHA_KEY: str = recaptcha_config['secret_key'] if 'secret_key' in recaptcha_config else ''
RECAPTCHA_USER_KEY: str = recaptcha_config['user_key'] if 'user_key' in recaptcha_config else ''
RECAPTCHA_VERIFY_URL: str = 'https://www.google.com/recaptcha/api/siteverify'

DATABASE_ROUTERS: List[str] = ['odm2cvs.db_routers.ControlledVocabularyRouter']
