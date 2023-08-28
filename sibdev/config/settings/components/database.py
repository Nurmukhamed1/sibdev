# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'sibdev',
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}

ALLOWED_IPS = [
    "127.0.0.1",
    "192.168.2.204",
]

ALLOWED_HOSTS = [
    "127.0.0.1",
    "192.168.2.204",
]
