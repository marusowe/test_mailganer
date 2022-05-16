# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from email_sender.models import Subscriber, EmailTemplate, EmailDelivery


class SubscriberAdmin(admin.ModelAdmin):
    pass


class EmailTemplateAdmin(admin.ModelAdmin):
    pass


class EmailDeliveryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Subscriber, SubscriberAdmin)
admin.site.register(EmailTemplate, EmailTemplateAdmin)
admin.site.register(EmailDelivery, EmailDeliveryAdmin)
