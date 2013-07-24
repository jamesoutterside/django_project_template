	# settiings/dev.py

from {{ project_name }}.settings.base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', 
		'NAME': os.path.join(VAR_ROOT, 'dev.db'),    
		}
}

INSTALLED_APPS += ("debug_toolbar",) 
INTERNAL_IPS = ("127.0.0.1")
MIDDLEWARE_CLASSES += ("debug_toolbar.middleware.DebugToolbarMiddleware")