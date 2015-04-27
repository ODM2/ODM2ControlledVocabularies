"""

WSGI config for odm2cvs project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'odm2cvs.settings.apache_sandbox'
os.environ['ODM2CVS_SECRET_KEY'] = 'thisisthenewkey'
os.environ['ODM2CVS_DATABASE_HOST'] = 'localhost'
os.environ['ODM2CVS_DATABASE_USER'] = 'django'
os.environ['ODM2CVS_DATABASE_PASSWORD'] = 'django4pp!'
os.environ['ODM2CVS_STATIC_ROOT'] = '/var/www/static/'

sys.path.append('/home/denver/projects/ODM2/src/odm2cvs')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
