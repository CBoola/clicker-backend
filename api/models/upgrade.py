# -*- coding: utf-8 -*-

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Upgrade(models.Model):

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
        upload_to="upgrades",
        verbose_name="Ikona")

    base_prize = models.IntegerField(
        default=1,
        validators=[MinValueValidator(1)],
        verbose_name="Cena bazowa")

    multiplier = models.IntegerField(
        default=1,
        validators=[MinValueValidator(1)],
        verbose_name="Mnożnik produkcji")

    class Meta:
        ordering = ['base_prize']
        verbose_name = "Ulepszenie"
        verbose_name_plural = "Ulepszenia"

    def __str__(self):
        return self.name
