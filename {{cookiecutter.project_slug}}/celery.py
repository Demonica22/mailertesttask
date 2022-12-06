import os
import celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mailertesttask.settings')
app = celery.Celery('mailertesttask')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
