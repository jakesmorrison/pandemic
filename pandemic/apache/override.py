#override.py

from pandemic.settings import *

DEBUG = False
ALLOWED_HOSTS = ['www.onemoretravelblog.com','onemoretravelblog.com', '192.241.228.71']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.sqlite3',
        'NAME': "/root/database/db_pandemic.sqlite3",
    }
}

