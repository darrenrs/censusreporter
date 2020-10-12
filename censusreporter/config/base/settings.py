# Django settings for censusreporter project.
import os

dirname = os.path.dirname
PROJECT_ROOT = os.path.abspath(os.path.join(dirname(__file__),"..",".."))

DEBUG = True
# should be set by each settings file
# ROOT_URLCONF = 'config.dev.urls'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'raven.contrib.django.raven_compat',
    'census',
)

ALLOWED_HOSTS = []
TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = False
USE_L10N = True
USE_TZ = True
SECRET_KEY = '!%j-u4&(q8qu4@dq=ukth27+q!v-!h^jck14bf=spqht847$4q'

MEDIA_ROOT = ''
MEDIA_URL = ''

STATIC_ROOT = PROJECT_ROOT + '/static/'
STATIC_URL = '/static/'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'census.context_processors.api_url',
            ],
        },
    },
]

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'censusreporter.wsgi.application'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
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

ADMINS = (
    ('Ian Dees', 'ian.dees@gmail.com'),
    ('Joe Germuska', 'joegermuska@gmail.com'),
    ('Ryan Pitts', 'ryan.a.pitts@gmail.com'),
)
MANAGERS = ADMINS

API_URL = os.environ.get('CENSUSREPORTER_API_URL', 'https://api.censusreporter.org')

import raven

RAVEN_CONFIG = {
    'dsn': os.environ.get("SENTRY_DSN"),
    'release': raven.fetch_git_sha(os.path.dirname(__file__) + '/../../..'),
}
