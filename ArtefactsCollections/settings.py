import os	
	
import django_heroku	


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)	
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))	


# Quick-start development settings - unsuitable for production	
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/	

# SECURITY WARNING: keep the secret key used in production secret!	
SECRET_KEY = '%5eb(f$&wufnauo%1f+rw4uw)p$!1ystqpay)vhz^8fp7zw)%a'	

# SECURITY WARNING: don't run with debug turned on in production!	
DEBUG = True	

ALLOWED_HOSTS = ["*"]	


# Application definition	

INSTALLED_APPS = [	
    'django.contrib.admin',	
    'django.contrib.auth',	
    'django.contrib.contenttypes',	
    'django.contrib.sessions',	
    'django.contrib.messages',	
    'django.contrib.staticfiles',	
    'django_forms_bootstrap',	
    'accounts',	
    'auctions',	
    'bids',	
    'home',	
    'products',	
    'reviews',	
    'basket',	
    'users',	
    'checkout',	
    'mathfilters',	
    'storages',	
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

ROOT_URLCONF = 'ArtefactsCollections.urls'	

TEMPLATES = [	
    {	
        'BACKEND': 'django.template.backends.django.DjangoTemplates',	
        'DIRS': [os.path.join(BASE_DIR, "templates")],	
        'APP_DIRS': True,	
        'OPTIONS': {	
            'context_processors': [	
                'django.template.context_processors.debug',	
                'django.template.context_processors.request',	
                'django.contrib.auth.context_processors.auth',	
                'django.contrib.messages.context_processors.messages',	
                'django.template.context_processors.media',	
                'basket.contexts.basket_contents'	

            ],	
        },	
    },	
]	

WSGI_APPLICATION = 'ArtefactsCollections.wsgi.application'	


# Database	
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases	

DATABASES = {	
    'default': {	
        'ENGINE': 'django.db.backends.sqlite3',	
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),	
    }	
}	


# Password validation	
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators	

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

AUTHENTICATION_BACKENDS = [	
    'django.contrib.auth.backends.ModelBackend',	
    'accounts.backends.EmailAuth',	
    ]	


# Internationalization	
# https://docs.djangoproject.com/en/1.11/topics/i18n/	

LANGUAGE_CODE = 'en-us'	

TIME_ZONE = 'UTC'	

USE_I18N = True	

USE_L10N = True	

USE_TZ = True	


# Static files (CSS, JavaScript, Images)	
# https://docs.djangoproject.com/en/1.11/howto/static-files/	


AWS_S3_OBJECT_PARAMETERS = {	
    'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',	
    'CacheControl': 'max-age=9460800',	
}	


AWS_STORAGE_BUCKET_NAME = 'denny-auctionsite'	
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")	
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")	


AWS_S3_HOST = 's3-eu-west-1.amazonaws.com'	
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME	


MEDIAFILES_LOCATION = 'media'	
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'	


MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)	
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')	



STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), )	
STATICFILES_LOCATION = 'static'	
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'	
STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)	




STRIPE_PUBLISHABLE = os.getenv("STRIPE_PUBLISHABLE")	
STRIPE_SECRET = os.getenv("STRIPE_SECRET")	


MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'