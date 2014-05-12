# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

TIME_ZONE = 'America/New_York'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# pretty important things
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
REGISTRATION_LOCK = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ohyou'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = DEBUG