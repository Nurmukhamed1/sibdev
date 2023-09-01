# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('POSTGRES_DB', 'sibdev'),
        "USER": os.getenv('POSTGRES_USER', 'postgres'),
        "PASSWORD": os.getenv('POSTGRES_PASSWORD', 'postgres'),
        "HOST": os.getenv('POSTGRES_HOST', '127.0.0.1'),
        "PORT": os.getenv('POSTGRES_PORT', '5432'),
    }
}

ALLOWED_IPS = ['*']

ALLOWED_HOSTS = ['*']
