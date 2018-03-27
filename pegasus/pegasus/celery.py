import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pegasus.settings')

from django.conf import settings

app = Celery('pegasus')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)