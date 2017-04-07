from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# -*- coding: utf-8 -*-

from django.db import models
from jsonfield import JSONField

from api.validators import validate_schema, validate_existence
from api.schemas import *

from api.models.structure import Structure
from api.models.upgrade import Upgrade


class Player(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        verbose_name="Nazwa gracza")

    current_state = JSONField(
        default={},
        blank=True,
        validators=[
            validate_schema(CURRENT_STATE_SCHEMA)
        ],
        verbose_name="Stan rozgrywki")

    structures = JSONField(
        default=[],
        blank=True,
        validators=[
            validate_schema(STRUCTURES_SCHEMA),
            validate_existence(Structure.objects.all())
        ],
        verbose_name="Posiadane struktury")

    upgrades = JSONField(
        default=[],
        blank=True,
        validators=[
            validate_schema(UPGRADES_SCHEMA),
            validate_existence(Upgrade.objects.all())
        ],
        verbose_name="Posiadane ulepszenia")

    statistics = JSONField(
        default={},
        blank=True,
        validators=[
            validate_schema(STATISTICS_SCHEMA)
        ],
        verbose_name="Statystyki")

    class Meta:
        verbose_name = "Gracz"
        verbose_name_plural = "Gracze"

    def __str__(self):
        return "{0} {1}".format(self.user.first_name, self.user.last_name)

    @staticmethod
    def is_user_logged(user):
        return user.is_authenticated() and not user.is_staff
