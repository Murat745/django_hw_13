from celery import shared_task

from django.core.mail import send_mail as django_send_mail


@shared_task
def send_email(text_reminder, to_email):
    django_send_mail(text_reminder, to_email)
