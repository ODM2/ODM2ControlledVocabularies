"""
Django settings for odm2cvs project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

try:
    SECRET_KEY = os.environ['ODM2CVS_SECRET_KEY']
    DATABASE_HOST = os.environ['ODM2CVS_DATABASE_HOST']
    DATABASE_USER = os.environ['ODM2CVS_DATABASE_USER']
    DATABASE_PASSWORD = os.environ['ODM2CVS_DATABASE_PASSWORD']
except KeyError:
    print "Please set the required environment variables ODM2CVS_SECRET_KEY, ODM2CVS_DATABASE_HOST, " \
          "ODM2CVS_DATABASE_USER, ODM2CVS_DATABASE_PASSWORD"
    exit(True)


ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
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
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'odm2cvs.urls'

WSGI_APPLICATION = 'odm2cvs.wsgi.wsgi.application'



# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'odm2cvsconfig',
        'USER': DATABASE_USER,
        'PASSWORD': DATABASE_PASSWORD,
        'HOST': DATABASE_HOST,
        'PORT': '3306',
    },
    'control_vocabularies': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'odm2cvs',
        'USER': DATABASE_USER,
        'PASSWORD': DATABASE_PASSWORD,
        'HOST': DATABASE_HOST,
        'PORT': '3306',
    }
}

# Internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, '../../templates'),
)

TASTYPIE_DEFAULT_FORMATS = ['json']

API_LIMIT_PER_PAGE = 0

DATABASE_ROUTERS = ['odm2cvs.db_routers.ControlVocabularyRouter']
