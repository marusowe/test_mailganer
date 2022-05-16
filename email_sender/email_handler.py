from __future__ import absolute_import
from django.utils import timezone

from django.core.mail import send_mail

from config import settings
from email_sender.models import EmailDelivery


class EmailHandler(object):
    @staticmethod
    def _prepare_email_message(message, user, message_id):
        message_text = message.format(**user)
        email_tracking = (
            '<img src="{domain}/email_tracking/{message_id}" height="0px" width="0px" />'.format(
            domain=settings.DOMAIN, message_id=message_id
        ))
        message = message_text + email_tracking
        return message

    def send_emails(self):
        emails = (
            EmailDelivery.objects.filter(is_send=False)
            .select_related("subscriber", "email_template")
            .order_by("scheduled_sending")[:10]
        )
        for email_data in emails:
            if (
                not email_data.scheduled_sending
                or email_data.scheduled_sending <= timezone.now()
            ):
                send_mail(
                    subject=email_data.email_template.subject,
                    message='',
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[email_data.subscriber.email],
                    html_message=self._prepare_email_message(
                        email_data.email_template.message,
                        email_data.subscriber.__dict__,
                        email_data.id,
                    ),
                )
                EmailDelivery.objects.filter(id=email_data.id).update(is_send=True)
