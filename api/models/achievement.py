# -*- coding: utf-8 -*-

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Achievement(models.Model):

    ACHIEVEMENT_TYPE = [
        ('NUMBER_OF_CLICKS', 'Ilość kliknięć'),
        ('COLLECTED_CASH', 'Zgromadzone pieniądze'),
        ('MAXIMUM_CASH', 'Maksymalna posiadana ilość pieniędzy'),
        ('SPENT_CASH', 'Łącznie wydane pieniądze'),
        ('OTHER', 'Inny')
    ]

    system_id = models.CharField(
        max_length=25,
        unique=True,
        verbose_name="Identyfikator")

    type = models.CharField(
        max_length=25,
        choices=ACHIEVEMENT_TYPE,
        unique=True,
        verbose_name="Typ")

    name = models.CharField(
        max_length=25,
        verbose_name="Nazwa")

    description = models.CharField(
        max_length=100,
        verbose_name="Opis")

    icon = models.FileField(
        upload_to="structures",
        verbose_name="Ikona")

    class Meta:
        ordering = ['type']
        verbose_name = "Osiągnięcie"
        verbose_name_plural = "Osiągnięcia"

    def __str__(self):
        return self.name
