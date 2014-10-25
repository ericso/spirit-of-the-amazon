"""
Django settings for amazon project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

# Appending parent directory b/c settings.py file is in config sub-dir
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates/')
if os.sep != '/':
  # Django says, "Always use forward slashes, even on Windows."
  TEMPLATE_DIR = TEMPLATE_DIR.replace(os.sep, '/')
TEMPLATE_DIRS = (
  TEMPLATE_DIR,
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_URL = os.path.join(BASE_DIR, 'static/')
CATALOG_STATIC_URL = os.path.join(BASE_DIR, 'static/catalog/')
STATICFILES_DIRS = (
  STATIC_URL,
  CATALOG_STATIC_URL,
)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEDIA_URL = '/media/'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^#0-$@+%_%)-tjgtt+s1hz59$b$ok-i-b1=%)1n^u_=gh95h)i'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition
DEFAULT_APPS = (
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',
  'django.contrib.flatpages',
  'django.contrib.sites',
)
THIRD_PARTY_APPS = (
  'django_nose',
)
LOCAL_APPS = (
  'catalog',
  'utils',
  'cart',
)
INSTALLED_APPS = DEFAULT_APPS + THIRD_PARTY_APPS + LOCAL_APPS


MIDDLEWARE_CLASSES = (
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.middleware.common.CommonMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
  'django.middleware.clickjacking.XFrameOptionsMiddleware',
  'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
  'SSLMiddleware.SSLRedirect',
)

TEMPLATE_CONTEXT_PROCESSORS = (
  "django.contrib.auth.context_processors.auth",
  "django.core.context_processors.debug",
  "django.core.context_processors.i18n",
  "django.core.context_processors.media",
  "django.core.context_processors.static",
  "django.core.context_processors.request",
  'django.contrib.messages.context_processors.messages',
  'utils.context_processors.amazon',
)

ROOT_URLCONF = 'amazon.urls'

WSGI_APPLICATION = 'amazon.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'amazon',
    'USER': 'amazonuser',
    'PASSWORD': 'amazonpassword',
    # 'HOST': 'localhost',
    # 'PORT': '3306',
  }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Site-specific meta information
SITE_NAME = 'Spirit of the Amazon'
SITE_ID = 1
META_KEYWORDS = 'Amazon, rain forest, photography, non-profit, selling'
META_DESCRIPTION = 'Spirit of the Amazon is a non-profit site where photographers can sell their photographs of the Amazon'

# Change to True before deploying to production
ENABLE_SSL = False

