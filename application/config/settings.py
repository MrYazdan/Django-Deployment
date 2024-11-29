from pathlib import Path
from decouple import config

USE_TZ = True
USE_I18N = True
MEDIA_URL = 'media/'
STATIC_URL = 'static/'
LANGUAGE_CODE = 'en-us'
ROOT_URLCONF = 'config.urls'
WSGI_APPLICATION = 'config.wsgi.application'
DEBUG = config("DEBUG", cast=bool, default=True)
BASE_DIR = Path(__file__).resolve().parent.parent
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
TIME_ZONE = config("TIME_ZONE", default="Asia/Tehran")
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
SECRET_KEY = config("SECRET_KEY", default="&(dj-development-secret_key)$")
ALLOWED_HOSTS = ["*"] if DEBUG else config("ALLOWED_HOSTS", cast=lambda hosts: hosts.split(','))
MEDIA_ROOT = BASE_DIR / 'storage/media'
STATIC_ROOT_PATH = BASE_DIR / "storage/static"
DEFAULT_FROM_EMAIL = config("EMAIL_DEFAULT_FROM", default="noreply@development.dev")

# Application
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

if DEBUG:
    # Static
    STATICFILES_DIRS = [
        STATIC_ROOT_PATH,
    ]

    # Email
    EMAIL_HOST = "localhost"
    EMAIL_PORT = 2525
    EMAIL_HOST_USER = ""
    EMAIL_HOST_PASSWORD = ""
    EMAIL_USE_TLS = False

    # Database
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

    # Cache
    CACHES = {
        "default": {
            "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
            "LOCATION": BASE_DIR / "tmp/cached_files",
        }
    }

    CORS_ALLOW_ALL_ORIGINS = True
else:
    # Statics
    STATIC_ROOT = STATIC_ROOT_PATH

    # Email
    EMAIL_HOST = config("EMAIL_HOST")
    EMAIL_PORT = config("EMAIL_PORT", cast=int)
    EMAIL_HOST_USER = config("EMAIL_HOST_USER")
    EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD")
    EMAIL_USE_TLS = config("EMAIL_USE_TLS", cast=bool)

    # Database
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': config("DB_NAME"),
            'USER': config("DB_USER"),
            'PASSWORD': config("DB_PASSWORD"),
            'PORT': config("DB_PORT"),
            'HOST': config("DB_HOST"),
        }
    }

    # Cache
    REDIS_HOST = config("REDIS_HOST")
    REDIS_PORT = config("REDIS_PORT")
    REDIS_URL = f"redis://{REDIS_HOST}:{REDIS_PORT}"
    CACHES = {
        "default": {
            "BACKEND": "django.core.cache.backends.redis.RedisCache",
            "LOCATION": REDIS_URL,
        }
    }

    # Security params:
    # SECURE_HSTS_SECONDS = 12 * 30 * 24 * 60 * 60
    # SECURE_HSTS_PRELOAD = True
    # SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    # SECURE_SSL_REDIRECT = True
    # SECURE_PROXY_SSL_HEADER = "HTTP_X_FORWARDED_PROTO" ,"https"
    # USE_X_FORWARDED_HOST = True
    # SESSION_COOKIE_SECURE = True
    # CSRF_COOKIE_SECURE = True
    # SECURE_REFERRER_POLICY = "strict-origin"
    # X_FRAME_OPTIONS = "SAMEORIGIN"
    # SESSION_COOKIE_AGE = 3 * 60 * 60
    # SESSION_TIMEOUT = 24 * 60 * 60

    # CORS params
    # CORS_ALLOW_ALL_ORIGINS = False
    # CORS_ALLOWED_ORIGINS = config(
    #     "ALLOWED_HOSTS",
    #     cast=lambda hosts: hosts.split(','),
    #     default="http://0.0.0.0:8000, http://localhost:8000"
    # )


AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            "style": "{",
            'format': "{levelname} {message}"
        },
        "verbose": {
            "style": "{",
            'format': "{levelname} {message} {asctime} {module} {message}"
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "simple"
        },
        "file": {
            "level": "ERROR",
            "class": "logging.FileHandler",
            "filename": "errors.log",
            "formatter": "verbose"
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console", "file"],
            "level": "INFO",
            "propagate": True
        }
    }
}

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ]
}