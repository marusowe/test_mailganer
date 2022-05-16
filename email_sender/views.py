# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from PIL.Image import new
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, View, FormView, RedirectView, CreateView

from email_sender.forms import EmailDeliveryForm
from email_sender.models import EmailTemplate, Subscriber, EmailDelivery


class MainView(TemplateView):
    template_name = "main.html"

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context["email_delivery"] = EmailDelivery.objects.select_related(
            "subscriber", "email_template"
        ).all()
        return context


class TrackingEmail(View):
    def get(self, *args, **kwargs):
        email_delivery = get_object_or_404(EmailDelivery, pk=kwargs["uuid"])
        email_delivery.is_open = True
        email_delivery.save()
        red = new("RGB", (1, 1))
        response = HttpResponse(content_type="image/png")
        red.save(response, "PNG")
        return response


class CreateSubscriberView(CreateView):
    model = Subscriber
    fields = ["name", "second_name", "birth_date", "email"]
    template_name = "subscriber.html"
    success_url = "/"


class CreateEmailTemplateView(CreateView):
    model = EmailTemplate
    fields = ["name", "subject", "message"]
    template_name = "email_template.html"
    success_url = "/"


class EmailDeliveryCreateView(FormView):
    template_name = "email_delivery.html"
    form_class = EmailDeliveryForm
    success_url = "/"

    def form_valid(self, form):
        form.save()
        return super(EmailDeliveryCreateView, self).form_valid(form)
