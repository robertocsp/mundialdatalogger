

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['52.72.157.127', '.thermoguardian.com.br', ]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mdltemp',
        'USER': 'mdltemp',
        'PASSWORD': 'mdltemp6556122020',
        'HOST': 'mdltemp.cszlzjei5yav.us-east-1.rds.amazonaws.com',
        'PORT': '5432',
    }
}

print('entrou no producao settings')




