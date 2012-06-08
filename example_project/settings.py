 # -*- coding: utf-8 -*-
import os

PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))

# ==============================================================================
# debug settings
# ==============================================================================

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'dev.db',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# ==============================================================================
# i18n and url settings
# ==============================================================================
TIME_ZONE = 'Europe/Paris'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'fr'

gettext = lambda s:s
LANGUAGES = (
        ('en',gettext(u'English')),
        ('fr',gettext(u'Français')),
)

SITE_ID = 1

USE_I18N = True
USE_L10N = True

MEDIA_ROOT = os.path.join(PROJECT_PATH,'public/mymedia/')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(PROJECT_PATH,'public/static')
STATIC_URL = '/static/'

ADMIN_MEDIA_PREFIX = '/static/admin/'
#ADMIN_MEDIA_PREFIX = '/static/grappelli/'
JCHAT_MEDIA_PREFIX = '/static/jchat/'

# Additional locations of static files
STATICFILES_DIRS = (
    #os.path.join(PROJECT_PATH, '../contrib/grappelli/static/'),
    #os.path.join(PROJECT_PATH, '../contrib/grappelli/templates/'),

    os.path.join(PROJECT_PATH, 'jchat/static/'),

)
# ==============================================================================
# application and middleware settings
# ==============================================================================

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    #'django.contrib.humanize',
    #'django.contrib.webdesign',
    'django_generic_flatblocks',
    'django_generic_flatblocks.contrib.gblocks',
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    "django.core.context_processors.static", 
    'django.core.context_processors.request',

)

TEMPLATE_DIRS = (
    os.path.join( PROJECT_PATH,'templates/'),
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#    'django.template.loaders.eggs.load_template_source',
)
ROOT_URLCONF = 'urls'
# ==============================================================================
# the secret key
# ==============================================================================
from random import choice
SECRET_KEY = ''.join([choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

