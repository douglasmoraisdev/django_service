"""
Django settings for app project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

USE_X_FORWARDED_HOST = True
FORCE_SCRIPT_NAME = '/homolog'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*7775v9*b08=h%w$elt@7fne1m#i5c)^um8ycj0!g%)3%*e4_e'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['https://us-east-2.console.aws.amazon.com', 'https://kruzmf4vb7.execute-api.us-east-2.amazonaws.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'polls.apps.PollsConfig',
    'django_s3_storage'
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

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
'''


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

DEFAULT_FILE_STORAGE = 'django_s3_storage.storage.S3Storage'

STATICFILES_STORAGE = "django_s3_storage.storage.StaticS3Storage"

AWS_REGION = "us-east-1"
AWS_S3_BUCKET_NAME = "static-django-service"
AWS_ACCESS_KEY_ID = "AKIA3S45XRFUYTT6QGTL"
AWS_SECRET_ACCESS_KEY = "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"
AWS_S3_ADDRESSING_STYLE = "auto"

AWS_S3_BUCKET_AUTH_STATIC = False
AWS_S3_BUCKET_NAME_STATIC = "static-django-service"

# The full URL to the S3 endpoint. Leave blank to use the default region URL.
AWS_S3_ENDPOINT_URL = ""

# A prefix to be applied to every stored file. This will be joined to every filename using the "/" separator.
AWS_S3_KEY_PREFIX = ""

# Whether to enable authentication for stored files. If True, then generated URLs will include an authentication
# token valid for `AWS_S3_MAX_AGE_SECONDS`. If False, then generated URLs will not include an authentication token,
# and their permissions will be set to "public-read".
AWS_S3_BUCKET_AUTH = False

# How long generated URLs are valid for. This affects the expiry of authentication tokens if `AWS_S3_BUCKET_AUTH`
# is True. It also affects the "Cache-Control" header of the files.
# Important: Changing this setting will not affect existing files.
AWS_S3_MAX_AGE_SECONDS = 60 * 60  # 1 hours.

# A URL prefix to be used for generated URLs. This is useful if your bucket is served through a CDN.
AWS_S3_PUBLIC_URL = ""

# If True, then files will be stored with reduced redundancy. Check the S3 documentation and make sure you
# understand the consequences before enabling.
# Important: Changing this setting will not affect existing files.
AWS_S3_REDUCED_REDUNDANCY = False

# The Content-Disposition header used when the file is downloaded. This can be a string, or a function taking a
# single `name` argument.
# Important: Changing this setting will not affect existing files.
AWS_S3_CONTENT_DISPOSITION = ""

# The Content-Language header used when the file is downloaded. This can be a string, or a function taking a
# single `name` argument.
# Important: Changing this setting will not affect existing files.
AWS_S3_CONTENT_LANGUAGE = ""

# A mapping of custom metadata for each file. Each value can be a string, or a function taking a
# single `name` argument.
# Important: Changing this setting will not affect existing files.
AWS_S3_METADATA = {}

# If True, then files will be stored using AES256 server-side encryption.
# If this is a string value (e.g., "aws:kms"), that encryption type will be used.
# Otherwise, server-side encryption is not be enabled.
# Important: Changing this setting will not affect existing files.
AWS_S3_ENCRYPT_KEY = False

# The AWS S3 KMS encryption key ID (the `SSEKMSKeyId` parameter) is set from this string if present.
# This is only relevant if AWS S3 KMS server-side encryption is enabled (above).
AWS_S3_KMS_ENCRYPTION_KEY_ID = ""

# If True, then text files will be stored using gzip content encoding. Files will only be gzipped if their
# compressed size is smaller than their uncompressed size.
# Important: Changing this setting will not affect existing files.
AWS_S3_GZIP = True

# The signature version to use for S3 requests.
AWS_S3_SIGNATURE_VERSION = None

# If True, then files with the same name will overwrite each other. By default it's set to False to have
# extra characters appended.
AWS_S3_FILE_OVERWRITE = False