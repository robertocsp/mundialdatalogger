from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mdltemphomologa',
        'USER': 'mdltemphomologa',
        'PASSWORD': 'mdltemphomologa',
        'HOST': 'mdltemphomologa.cszlzjei5yav.us-east-1.rds.amazonaws.com',
        'PORT': '5432',
    }
}

OUTPUTDIR = '/tmp/email-test'

print('entrou no homologa settings')