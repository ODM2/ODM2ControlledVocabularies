from odm2cvs.settings.base import *

DEBUG = True
TEMPLATE_DEBUG = True

WSGI_APPLICATION = 'odm2cvs.wsgi.windows_development.application'

DATABASES['default']['ENGINE'] = 'mysql.connector.django'
DATABASES['control_vocabularies']['ENGINE'] = 'mysql.connector.django'

STATIC_URL = '/static/'
SITE_URL = ''