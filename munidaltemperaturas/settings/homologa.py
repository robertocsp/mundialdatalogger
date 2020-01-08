from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mdlhomologa',
        'USER': 'mdlhomologa',
        'PASSWORD': 'mdlhomologa',
        'HOST': 'mdlhomologa.cszlzjei5yav.us-east-1.rds.amazonaws.com',
        'PORT': '5432',
    }
}


print('entrou no homologa settings')