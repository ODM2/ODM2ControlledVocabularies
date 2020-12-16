from odm2cvs.settings.base import *

DEBUG: bool = config['debug_mode']

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
if 'host' in config:
    ALLOWED_HOSTS.append(config.get('host'))
if 'host_alias' in config:
    ALLOWED_HOSTS.extend(config.get('host_alias'))

SITE_ROOT: str = config.get('site_root', '')
SITE_URL: str = ''
