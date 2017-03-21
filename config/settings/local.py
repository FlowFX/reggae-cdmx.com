from .common import *

DEBUG = True

INSTALLED_APPS += ['debug_toolbar',]


MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware',]


STATIC_URL = '/static/'
STATIC_ROOT = '/var/www/static/reggae-cdmx.com/'

MEDIA_URL = '/media/'
MEDIA_ROOT = '/var/www/media/reggae-cdmx.com/'