# coding=utf-8
from __future__ import unicode_literals

from settings import *

DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": os.path.join(BASE_DIR, "test.sqlite3"),}}
