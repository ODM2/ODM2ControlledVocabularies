"""

WSGI config for odm2cvs project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/

"""

import os
import sys

from django.core.wsgi import get_wsgi_application

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(BASE_DIR, os.pardir))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'odm2cvs.settings')

application = get_wsgi_application()