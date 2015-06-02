"""

WSGI config for odm2cvs project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/

"""

import os
import sys

from odm2cvs.settings.base import BASE_DIR

PROJECT_BASE = os.path.join(BASE_DIR, os.pardir)
sys.path.append(PROJECT_BASE)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
