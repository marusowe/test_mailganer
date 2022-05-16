from django.conf.urls import url

from email_sender.views import (
    TrackingEmail,
    EmailDeliveryCreateView,
    CreateSubscriberView,
    CreateEmailTemplateView,
    MainView,
)

urlpatterns = [
    url(
        r"^email_tracking/(?P<uuid>[0-9a-z-]+)$",
        TrackingEmail.as_view(),
        name="email_tracking",
    ),
    url(r"^subscriber/$", CreateSubscriberView.as_view(), name="create_subscriber"),
    url(r"^template/$", CreateEmailTemplateView.as_view(), name="create_template"),
    url(
        r"^email_delivery/$",
        EmailDeliveryCreateView.as_view(),
        name="create_email_delivery",
    ),
    url(r"^$", MainView.as_view(), name="main"),
]
