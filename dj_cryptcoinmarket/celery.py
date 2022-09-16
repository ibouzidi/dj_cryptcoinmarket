import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dj_cryptcoinmarket.settings')

app = Celery('dj_cryptcoinmarket')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'get_coins_data_30s': {
        'task': 'coins.tasks.get_coins_data',
        'schedule': 10.0
    }
}

app.autodiscover_tasks()