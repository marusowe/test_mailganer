from celery import shared_task

from email_sender.email_handler import EmailHandler


@shared_task
def send_emails():
    EmailHandler().send_emails()
