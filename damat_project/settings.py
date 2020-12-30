"""
Django settings for damat_project project.

Generated by 'django-admin startproject' using Django 3.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
from django.urls import reverse_lazy




# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'jfkvf2s**(gyc3-*g4as8m_z7a5no$071yldii+i=yy3_$x7c+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

APPS = [
    'modeltranslation', 
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
APPS.insert(0, 'jet.dashboard',)

APPS.insert(0, 'jet')


CUSTOME_APPS = [
    # 'rest_framework', 
    'account',
    'blog',
    'contact.apps.ContactConfig',
    'product.apps.ProductConfig',
    'index',
    'menu',
    'order',
    # 'mptt',
    # 'modeltrans',
]


THIRD_PARTY_APPS = [
    'social_django',
    'phonenumber_field',
    'rest_framework',
    'rest_framework.authtoken',

    # CORS
    # 'corsheaders',
]

INSTALLED_APPS = APPS + CUSTOME_APPS + THIRD_PARTY_APPS


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'damat_project.middleware.force_default_middleware.force_default_language_middleware',
    'django.middleware.locale.LocaleMiddleware', 
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # # CORS
    # 'corsheaders.middleware.CorsMiddleware',
    # 'django.middleware.common.CommonMiddleware',
]


#CORS
CORS_ORIGIN_ALLOW_ALL = True
# CORS_ORIGIN_WHITELIST = (
#     'http://localhost:8080',
# )



ROOT_URLCONF = 'i18n.urls'


# ROSETTA_MESSAGES_SOURCE_LANGUAGE_CODE = 'az'

# ROSETTA_MESSAGES_SOURCE_LANGUAGE_CODE = 'az'
USE_I18N = True 
USE_L10N = True



ROOT_URLCONF = 'damat_project.urls'

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
                'django.template.context_processors.media',

            ],
        },
    },
]

WSGI_APPLICATION = 'damat_project.wsgi.application'

AUTH_USER_MODEL = 'account.User'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'damats_db',
        'USER': 'admin_damat',
        'PORT': 5435,
        'PASSWORD': 'elvin123',
        'HOST': '127.0.0.1',
    }
}



# SCOIAL AUTH CONFIGRATION

AUTHENTICATION_BACKENDS = [
    # 'social_core.backends.linkedin.LinkedinOAuth2',
    # 'social_core.backends.instagram.InstagramOAuth2',
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
]


SOCIAL_AUTH_FACEBOOK_KEY = '219950869707977'       # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = '1f1682843bb8cedfae6beb09cd64b8b2'  # App Secret

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '871788835099-4buoe7ru6d3s0bt4qmshll7qi9fdkb43.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '6K0zpu08FvWqJsBVNL5B6BrD'


SOCIAL_AUTH_FACEBOOK_SCOPE = ['email', 'user_friends'] # add this
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'fields': 'id,name,email,picture',
}

SOCIAL_AUTH_URL_NAMESPACE = 'social' # namespace

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.social_auth.associate_by_email',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',

    'account.tools.social_auth.update_user_social_data', # custom pipeline
)



#REST API AUTHENTICATION USER FOR API
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
    # 'DEFAULT_PERMISSION_CLASSES': ( 'rest_framework.permissions.AllowAny', ),
}


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
LANGUAGE_CODE = 'tr'

gettext = lambda s: s
LANGUAGES = [
    ('tr', gettext('Turkish')),
    ('az', gettext('Azerbaijan')),
    ('ar', gettext('Arabic')),
    ('ru', gettext('Russian')),
    ('it', gettext('Italian')),
    ('en', gettext('English')),
]

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/


STATIC_URL = '/static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MODELTRANSLATION_DEFAULT_LANGUAGE = 'tr'
MODELTRANSLATION_LANGUAGES = ('tr', 'en', 'az', 'ar', 'ru', 'it', )
MODELTRANSLATION_FALLBACK_LANGUAGES = ('tr', 'en', 'tr', 'ar', 'ru', 'it', )
MODELTRANSLATION_PREPOPULATE_LANGUAGE = 'tr'
MODELTRANSLATION_TRANSLATION_FILES = (
    "product.translation",
)
# MODELTRANSLATION_CUSTOM_FIELDS = ( ) 
# MODELTRANSLATION_AUTO_POPULATE = False
# MODELTRANSLATION_DEBUG = False
# MODELTRANSLATION_ENABLE_FALLBACKS = True
# MODELTRANSLATION_LOADDATA_RETAIN_LOCALE = True



LOGIN_URL = reverse_lazy('account:login')

LOGIN_REDIRECT_URL = reverse_lazy('index:home') # login olandan sora redirect olacaq sehife
LOGOUT_REDIRECT_URL = reverse_lazy('index:home') # logout olandan sora redirect olacaq sehife

LOGOUT_URL = reverse_lazy('account:logout')




#FOR SEND EMAIL
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'tech.academy.docker@gmail.com'
EMAIL_HOST_PASSWORD = 'suqmnhaxezvemyhn'

# # config/settings.py
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend' # new
# DEFAULT_FROM_EMAIL = 'husubayli@gmail.com'
# EMAIL_HOST = 'smtp.sendgrid.net' # new
# EMAIL_HOST_USER = 'apikey' # new
# EMAIL_HOST_PASSWORD = '<sendgrid_password>' # new
# EMAIL_PORT = 587 # new
# EMAIL_USE_TLS = True # new