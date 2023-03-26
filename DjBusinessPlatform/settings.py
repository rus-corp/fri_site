"""
Django settings for DjBusinessPlatform project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6y7mrlc4z2!y7b6uv)3rvu%my38b%6nr78yl4l2c!*x$f+x2$i'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.sites',  # это нужно для корректной работы flatpages.
    'django.contrib.flatpages',
    'ckeditor',
    'ckeditor_uploader',
    'captcha',
    'mptt',
    'django_mptt_admin',
    'django_celery_beat',                                        # планировщик задач

    'app_users.apps.AppUsersConfig',                             #целиковый аккаунт пользователя
    'app_ads.apps.AppAdsConfig',                                 #объявления
    'app_static_pages.apps.AppStaticPagesConfig',                #загрузка доков в бд для редактирования
    'app_settings.apps.AppSettingsConfig',                       #добавление соцсетей и компаний
    'app_survey.apps.AppSurveyConfig',                           #голосование
    'app_news.apps.AppNewsConfig',                               #раздел новости
    'app_personal_account.apps.AppPersonalAccountConfig',        #пополнение лиц.счета
    'app_referral_program.apps.AppReferralProgramConfig',        #рефералка
    'app_tickets.apps.AppTicketsConfig',
    'app_portfolio.apps.AppPortfolioConfig',

]
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'  # планировщик задач
SITE_ID = 1  # это нужно для корректной работы flatpages.
CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.math_challenge'
CAPTCHA_FOREGROUND_COLOR = 'blue'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',  # локализация
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',  # flatpages
]

ROOT_URLCONF = 'DjBusinessPlatform.urls'

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

                'app_settings.context_proccessors.load_settings',  # настройки из админки
                'app_survey.context_proccessors.load_number_polls',  # кол-во новых голосований
            ],
        },
    },
]

WSGI_APPLICATION = 'DjBusinessPlatform.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'fl',
        'USER': 'postgres',
        'PASSWORD': '2909',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
AUTH_USER_MODEL = 'app_users.CustomUser'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # Убрать на продакшн
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = [
    ('ru', 'rus'),
    ('en', 'eng'),
]

LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale/')]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
# STATIC_ROOT = os.path.join(BASE_DIR, "static")

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEDIA_URL = '/media/'
FIXTURE_DIRS = (
    os.path.join(BASE_DIR, 'fixtures'),
)

# CKEditor Settings
CKEDITOR_UPLOAD_PATH = 'uploads/'
# CKEDITOR_BASEPATH = "/assets/ckeditor/ckeditor/"
CKEDITOR_IMAGE_BACKEND = "pillow"
CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'

CKEDITOR_CONFIGS = {
    'default':
        {
            'toolbar': 'full',
            'width': 'auto',
            'extraPlugins': ','.join([
                'codesnippet',
            ]),
        },
}