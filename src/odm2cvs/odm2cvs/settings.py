"""
Django settings for odm2cvs project.

To set the environment variables:
    1. rename .env_template file to .env
    2. then set the values in the .env file for all the variables
"""


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import socket

import environ

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Initialise environment variables
env = environ.Env()
environ.Env.read_env()

SECRET_KEY = env('SECRET_KEY')
RECAPTCHA_KEY = env('RECAPTCHA_KEY')
RECAPTCHA_USER_KEY = env('RECAPTCHA_USER_KEY')
RECAPTCHA_VERIFY_URL = "https://www.google.com/recaptcha/api/siteverify"
DEPLOY_TYPE = env('DEPLOYMENT_TYPE', default='prod')

DEBUG = DEPLOY_TYPE != 'prod'

PROXY_BASE_URL = 'http://127.0.0.1:8000'
if DEPLOY_TYPE == 'local':
    ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
else:
    # deploying to AWS ELB (Elastic Beanstalk)
    # This is necessary for AWS ELB Health Checks to pass.
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    PROXY_BASE_URL = env('PROXY_BASE_URL', default=PROXY_BASE_URL)
    ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=[PROXY_BASE_URL]) + [local_ip]

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
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# DATABASE SETTINGS
if DEPLOY_TYPE == 'local':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': env('DB_NAME'),
            'USER': env('DB_USER'),
            'PASSWORD': env('DB_PASSWORD'),
            'HOST': env('DB_HOST'),
            'PORT': env('DB_PORT'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': env('RDS_DB_NAME'),
            'USER': env('RDS_USERNAME'),
            'PASSWORD': env('RDS_PASSWORD'),
            'HOST': env('RDS_HOSTNAME'),
            'PORT': env('RDS_PORT'),
        }
    }


STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
}

# Password validation
# https://docs.djangoproject.com/en/3.2/topics/auth/passwords/#enabling-password-validation

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

# TASTYPIE SETTINGS
TASTYPIE_DEFAULT_FORMATS = ['json']

API_LIMIT_PER_PAGE = 0

# EMAIL SETTINGS
# TODO: (Pabitra) This email host is not going to work if the app is deployed to a server outside of USU (e.g., AWS)
EMAIL_HOST = 'mail.usu.edu'

EMAIL_SENDER = env('EMAIL_SENDER')
EMAIL_RECIPIENTS = env.list('EMAIL_RECIPIENTS')

if DEPLOY_TYPE == 'local':
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# STATIC FILES SETTINGS

# NOTE: The value set for STATIC_ROOT here has a dependency on the configuration of the Elastic Beanstalk (see file
# .ebextensions/django.config).
STATIC_ROOT = "staticfiles"
STATIC_URL = '/static/'
SITE_URL = ''
STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)

# LOGIN/OUT SETTINGS
LOGIN_URL = 'login'
# Redirect to home URL after login (Default redirects to /accounts/profile/)
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# SECURITY SETTINGS FOR NON-LOCAL DEPLOYMENTS
# if DEPLOY_TYPE != 'local':
#     CSRF_COOKIE_SECURE = True
#     CSRF_COOKIE_HTTPONLY = True
#
#     SECURE_HSTS_SECONDS = 60 * 60 * 24 * 7 * 52  # one year
#     SECURE_HSTS_INCLUDE_SUBDOMAINS = True
#     SECURE_HSTS_PRELOAD = True
#     SECURE_SSL_REDIRECT = True
#     SECURE_BROWSER_XSS_FILTER = True
#     SECURE_CONTENT_TYPE_NOSNIFF = True
#     SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
#
#     SESSION_COOKIE_SECURE = True

