"""

WSGI config for odm2cvs project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/

"""

import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(BASE_DIR, os.pardir))

from django.core.wsgi import get_wsgi_application
#application = get_wsgi_application()

def application(environ, start_response):
    os.environ['DJANGO_SETTINGS_MODULE'] = environ.get('DJANGO_SETTINGS_MODULE', '')
    return get_wsgi_application()(environ, start_response)
