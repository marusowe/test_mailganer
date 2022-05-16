from django import forms

from email_sender.models import Subscriber, EmailTemplate, EmailDelivery


class EmailDeliveryForm(forms.ModelForm):
    subscribers = forms.ModelMultipleChoiceField(queryset=Subscriber.objects.all())
    scheduled_sending = forms.CharField(
        required=False,
        widget=forms.widgets.DateTimeInput(attrs={"type": "datetime-local"}),
    )

    def save(self, commit=True):
        emails_delivery = []
        email_template = self.cleaned_data.get("email_template", None)
        scheduled_sending = self.cleaned_data.get("scheduled_sending", None)
        for subscriber in self.cleaned_data.get("subscribers", None):
            emails_delivery.append(
                EmailDelivery(
                    email_template=email_template,
                    subscriber=subscriber,
                    scheduled_sending=scheduled_sending if scheduled_sending else None,
                )
            )
        EmailDelivery.objects.bulk_create(emails_delivery)

    class Meta:
        model = EmailDelivery
        fields = ("email_template", "scheduled_sending")
