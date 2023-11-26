from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_hello_email_task(email):
    send_mail(
        'Welcome to Library',
        'Thank you so much for registration. Hope you won\'t regret it!',
        'library@mail.com',
        [email]
    )
