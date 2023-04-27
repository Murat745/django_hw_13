import os

from celery import Celery
from celery.schedules import crontab

from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

app = Celery("core")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
app.conf.timezone = settings.TIME_ZONE

app.conf.beat_schedule = {
    "add-every-odd-hour": {
        "task": "celery_email.tasks.parse_quote",
        "schedule": crontab(hour='1-23/2'),
    }
}
