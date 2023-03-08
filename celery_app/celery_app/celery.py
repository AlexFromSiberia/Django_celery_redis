import os
from celery import Celery
from celery.schedules import crontab

# Сделать переменную в settings.py доступной во всём проекте
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_app.settings')

app = Celery('celery_app')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# celery beat tasks

# app.conf.beat_schedule = {
#     'send-spam-every-10-min': {
#         'task': 'main.tasks.send_beat_email',
#         'schedule': crontab(minute='*/10'),
#     },
# }

