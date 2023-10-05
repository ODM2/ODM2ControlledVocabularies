from base import *

ALLOWED_HOSTS = [
    '.vocabulary.odm2.org',
    '.vocabulary.odm2.org.',
]

DEBUG = False
TEMPLATE_DEBUG = False

STATIC_ROOT = data['static_root']
STATIC_URL = '/static/'
SITE_URL = ''

