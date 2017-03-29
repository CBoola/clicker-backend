# -*- coding: utf-8 -*-

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Structure(models.Model):

    system_id = models.CharField(
        max_length=25,
        unique=True,
        verbose_name="Identyfikator")

    name = models.CharField(
        max_length=25,
        verbose_name="Nazwa")

    description = models.CharField(
        max_length=100,
        verbose_name="Opis")

    icon = models.ImageField(
        upload_to="structures",
        verbose_name="Ikona")

    base_prize = models.IntegerField(
        default=1,
        validators=[MinValueValidator(1)],
        verbose_name="Cena bazowa")

    production_rate = models.IntegerField(
        default=1,
        validators=[MinValueValidator(1)],
        verbose_name="Szybkość produkcji")

    class Meta:
        ordering = ['base_prize']
        verbose_name = "Struktura"
        verbose_name_plural = "Struktury"

    def __str__(self):
        return self.name
