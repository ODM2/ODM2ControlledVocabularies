from odm2cvs.settings.base import *


DEBUG: bool = True

INTERNAL_IPS: Tuple[str] = (
    '127.0.0.1',
)

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
SITE_URL: str = ''
