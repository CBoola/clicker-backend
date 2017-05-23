# -*- coding: utf-8 -*-

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Achievement(models.Model):

    ACHIEVEMENT_TYPE = [
        ('BOUGHT_STRUCTURES', 'Kupione struktury'),
        ('SPENT_CASH', 'Wydane pieniądze'),
        ('MAXIMUM_CASH', 'Posiadane pieniędze'),
        ('OTHER', 'Inny')
    ]

    system_id = models.CharField(
        max_length=25,
        unique=True,
        verbose_name="Identyfikator")

    type = models.CharField(
        max_length=100,
        choices=ACHIEVEMENT_TYPE,
        verbose_name="Typ")

    related_system_id = models.CharField(
        max_length=25,
        default="",
        null=True,
        blank=True,
        verbose_name="Identyfikator modelu relacji",
        help_text="""Identyfikator do jakiegokolwiek modelu zadeklarowanego w systemie
            (jego poprawność nie jest sprawdzana).""")

    name = models.CharField(
        max_length=100,
        verbose_name="Nazwa")

    description = models.CharField(
        max_length=200,
        verbose_name="Opis")

    icon = models.FileField(
        upload_to="structures",
        verbose_name="Ikona")

    threshold = models.IntegerField(
        default=1,
        validators=[MinValueValidator(1)],
        verbose_name="Próg zdobycia")

    class Meta:
        ordering = ['type']
        verbose_name = "Osiągnięcie"
        verbose_name_plural = "Osiągnięcia"

    def __str__(self):
        return self.name
