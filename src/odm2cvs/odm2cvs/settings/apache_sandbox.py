from base import *

DEBUG = True
TEMPLATE_DEBUG = True

STATIC_ROOT = env('STATIC_ROOT')
STATIC_URL = '/static/'
SITE_URL = ''

#logging.basicConfig(level = logging.INFO, format = '%(asctime)s %(levelname)s %(message)s', filename = '/var/log/django/django.log',)
