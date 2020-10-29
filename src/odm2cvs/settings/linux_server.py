from odm2cvs.settings.base import *

DEBUG: bool = config['debug_mode']

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
if "host" in config:
    ALLOWED_HOSTS.append(config["host"])
if "host_alias" in config:
    ALLOWED_HOSTS.extend(config["host_alt"])

STATIC_ROOT: str = config["static_root"]
SITE_ROOT: str = config["site_root"]
STATIC_URL: str = config["static_url"]
SITE_URL: str = ''
