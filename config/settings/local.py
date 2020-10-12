from .base import *

SECRET_KEY = config('SECRET_KEY', default='MY_SUPER_SECRET_KEY')
DJANGO_ADMIN_URL = config('DJANGO_ADMIN_URL', default='admin/')


# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ["*"]

CORS_ORIGIN_ALLOW_ALL = True

CORS_ORIGIN_WHITELIST = [
    "http://localhost:8000"
]

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = ""
EMAIL_PORT = 25
EMAIL_USE_TLS = False
EMAIL_USE_SSL = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
    # 'default': {
    #     "ENGINE": config("DB_ENGINE", default="django.db.backends.sqlite3"),
    #     "NAME": config("DB_NAME", default=os.path.join(BASE_DIR, "db.sqlite3")),
    #     "USER": config("DB_USER"),
    #     "PASSWORD": config("DB_PASSWORD"),
    #     "HOST": config("DB_HOST"),
    #     "PORT": config("DB_PORT"),
    #     "OPTIONS": {
    #         'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
    #     }
    # }
}

# WhiteNoise
# ------------------------------------------------------------------------------
# http://whitenoise.evans.io/en/latest/django.html#using-whitenoise-in-development
INSTALLED_APPS = [  # noqa: F405
                 ] + INSTALLED_APPS  # noqa: F405

INTERNAL_IPS = ["127.0.0.1", "10.0.2.2"]


REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': int(os.getenv('DJANGO_PAGINATION_LIMIT', 1000)),
    'DATE_INPUT_FORMATS': ['iso-8601', '%Y-%m-%dT%H:%M:%S.%fZ'],
    'DEFAULT_RENDERER_CLASSES': (
        'djangorestframework_camel_case.render.CamelCaseJSONRenderer',
        'djangorestframework_camel_case.render.CamelCaseBrowsableAPIRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        # If you use MultiPartFormParser or FormParser, we also have a camel case version
        'djangorestframework_camel_case.parser.CamelCaseFormParser',
        'djangorestframework_camel_case.parser.CamelCaseMultiPartParser',
        'djangorestframework_camel_case.parser.CamelCaseJSONParser',
        # Any other parsers
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # 'rest_framework.authentication.SessionAuthentication',
        'tespk.tespk_auth.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_MODEL_SERIALIZER_CLASS': 'drf_toolbox.serializers.ModelSerializer',
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema'
}


# LOGGING
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#logging
# See https://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    "version": 1,
        "disable_existing_loggers": False,
        "loggers": {
                'main': {
                    'level': 'DEBUG',
                    'handlers': ['file'],
                    'propagate': True,
                }
            },
        "handlers": {
            "file": {
                "level": "DEBUG",
                "class": "logging.handlers.TimedRotatingFileHandler",
                "filename": os.path.join(BASE_DIR, "logs/tespk.log"),
                'when': 'midnight',  # this specifies the interval(roll over set to midnight)
                'interval': 1,  # defaults to 1, only necessary for other values
                'backupCount': 10,  # how many backup file to keep, 10 days
                "formatter": "verbose",
            }
        },
        "formatters": {
            "verbose": {
                "format": "%(levelname)s %(asctime)s %(module)s "
                          "%(process)d %(thread)d %(message)s"
            }
        }
}
# Your stuff...
# ------------------------------------------------------------------------------

# Webpack
WEBPACK_LOADER = {
    "DEFAULT": {
        "CACHE": not DEBUG,  # on DEBUG should be False
        "BUNDLE_DIR_NAME": 'webpack_bundles/',  # must end with slash
        "STATS_FILE": "tespk/frontend/assets/webpack_bundles/webpack-stats.dev.json",
        "POLL_INTERVAL": 0.1,
        "TIMEOUT": None,
        "IGNORE": [".+\.hot-update.js", ".+\.map"],
        'LOADER_CLASS': 'webpack_loader.loader.WebpackLoader',
    }
}

