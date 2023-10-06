"""
Django settings for odm2cvs project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/

To setup the settings json file:
    1. rename settings_template.json to settings.json
    2. then write all the necessary data in it
    3. ???
    4. Profit!
"""


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

data = {}
try:
    with open(os.path.join(BASE_DIR, 'settings', 'settings.json')) as data_file:
        data = json.load(data_file)
except IOError:
    print("You need to setup the settings data file (see instructions in base.py file.)")


try:
    SECRET_KEY = data["secret_key"]
except KeyError:
    print("The secret key is required in the settings.json file.")
    exit(1)

RECAPTCHA_KEY = data["recaptcha_secret_key"] if "recaptcha_secret_key" in data else ""
RECAPTCHA_USER_KEY = data["recaptcha_user_key"] if "recaptcha_user_key" in data else ""
RECAPTCHA_VERIFY_URL = "https://www.google.com/recaptcha/api/siteverify"

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tastypie',
    'cvservices',
    'cvinterface',
    'rdfserializer',
    'widget_tweaks',
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

ROOT_URLCONF = 'odm2cvs.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
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

WSGI_APPLICATION = 'odm2cvs.wsgi.application'


# Databases
DATABASES = {}
for database in data['databases']:
    DATABASES[database['name']] = {
        'ENGINE': database['engine'],
        'NAME': database['schema'],
        'USER': database['user'] if 'user' in database else '',
        'PASSWORD': database['password'] if 'password' in database else '',
        'HOST': database['host'] if 'host' in database else '',
        'PORT': database['port'] if 'port' in database else '',
        'OPTIONS': database['options'] if 'options' in database else ''
    }

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


TASTYPIE_DEFAULT_FORMATS = ['json']

API_LIMIT_PER_PAGE = 0


EMAIL_HOST = 'mail.usu.edu'

EMAIL_SENDER = data['email_sender'] if 'email_sender' in data else '',
EMAIL_SENDER = EMAIL_SENDER[0] if isinstance(EMAIL_SENDER, tuple) else EMAIL_SENDER

EMAIL_RECIPIENTS = list(data['email_recipients']) if 'email_recipients' in data else [],
EMAIL_RECIPIENTS = EMAIL_RECIPIENTS[0] if isinstance(EMAIL_RECIPIENTS, tuple) else EMAIL_RECIPIENTS

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

DATABASE_ROUTERS = ['odm2cvs.db_routers.ControlledVocabularyRouter']

LOGIN_URL = 'login'

# Redirect to home URL after login (Default redirects to /accounts/profile/)
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

