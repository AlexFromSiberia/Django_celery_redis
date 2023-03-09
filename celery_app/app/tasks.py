from celery_app.celery import app
from django.core.mail import send_mail
from celery_app.settings import EMAIL_HOST_USER


@app.task
def send_spam_email(user_email):
    send_mail(
        'Тут будет тема сообщения',
        'Тут будет текст сообщения',
        EMAIL_HOST_USER,
        [user_email],
        fail_silently=False,
    )





