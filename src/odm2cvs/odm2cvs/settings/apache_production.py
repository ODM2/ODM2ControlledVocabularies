from odm2cvs.settings.base import *

ALLOWED_HOSTS = [
    '.vocabulary.odm2.org',
    '.vocabulary.odm2.org.',
]

DEBUG = False
TEMPLATE_DEBUG = False

STATIC_ROOT = os.environ['ODM2CVS_STATIC_ROOT']
STATIC_URL = '/static/'
SITE_URL = ''

