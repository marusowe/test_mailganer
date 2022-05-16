# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid

from django.db import models


class Subscriber(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    second_name = models.CharField(max_length=100, verbose_name="Фамилия")
    birth_date = models.DateField(verbose_name="Дата рождения")
    email = models.EmailField(verbose_name="Email")

    def __unicode__(self):
        return self.email

    class Meta:
        verbose_name_plural = "Подписчики рассылки"
        verbose_name = "Подписчик рассылки"


class EmailTemplate(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название")
    subject = models.TextField(verbose_name="Тема")
    message = models.TextField(verbose_name="Шаблон")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Шаблоны писем"
        verbose_name = "Шаблон письма"


class EmailDelivery(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    subscriber = models.ForeignKey(
        Subscriber, on_delete=models.CASCADE, verbose_name="Подписчик"
    )
    email_template = models.ForeignKey(
        EmailTemplate, on_delete=models.CASCADE, verbose_name="Шаблон"
    )
    scheduled_sending = models.DateTimeField(
        null=True, verbose_name="Запланированное время и дата отправления"
    )
    is_send = models.BooleanField(default=False, verbose_name="Письмо отправлено")
    is_open = models.BooleanField(default=False, verbose_name="Письмо прочитано")

    def __unicode__(self):
        return self.subscriber.name

    class Meta:
        verbose_name_plural = "Рассылка писем"
        verbose_name = "Рассылка писем"
