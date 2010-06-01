#!/usr/bin/env python
# -*- coding: utf-8 -*-

#   Django settings for cis project.
import os.path
# getting the path of the project
# to auto-detect the absolute path
# of the tamplate folder, when project moved.
PROJECT_DIR = os.path.dirname(__file__)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
    ('John F. Mukulu', 'john.f.mukulu@gmail.com'),
    ('Allen Machary', 'allen.machary@gmail.com'),
    ('Salome H. Maro', 'your_email@domain.com'),
    ('Irene Togolai', 'your_email@domain.com'),
    ('Amrany Mlawa', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'mysql'       # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'cis'		# Using this for mysql db system
DATABASE_USER = 'root'          # Using this for mysql db system
# dont database password here
DATABASE_PASSWORD = 'root'          # Using this for mysql db system
DATABASE_HOST = ''              # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''              # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Africa/Dar_es_salaam'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/static'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'm7*_*%d5+=95xy^+lllx90^il(c=w+*wfjm9)!ndrl3apj-9lc'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.locale.LocaleMiddleware',
)

ROOT_URLCONF = 'cis.urls'

TEMPLATE_CONTEXT_PROCESSORS = [
    "django.core.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    "core.context_processors.base_template" # sticks the base template inside all responses
]


TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_DIR, 'templates')
)

# this is the template that is used as the base for all
# cis pages.  if you want to totally restyle your pages
BASE_TEMPLATE =  "core-layout.html"

# This is a similar concept, but for templating the login
# and logout screens
LOGIN_TEMPLATE = "core/login.html"

LOGGEDOUT_TEMPLATE = "core/loggedout.html"

LOGIN_REDIRECT_URL = "/dashboard/"

# serves css, javascript, images
STATIC_DOC_ROOT = os.path.join(PROJECT_DIR, 'core/static')

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'cis.book',
    'cis.investigation',
    'cis.locations',
    'cis.offenses',
    'cis.core',
)
