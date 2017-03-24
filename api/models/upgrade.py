from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Upgrade(models.Model):

    system_id = models.CharField(max_length=25, unique=True)
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=100)
    icon = models.ImageField(upload_to="upgrades")

    base_prize = models.IntegerField(
        default=1,
        validators=[MinValueValidator(1)])
    multiplier = models.IntegerField(
        default=1,
        validators=[MinValueValidator(1)])

    class Meta:
        ordering = ['base_prize']

    def __str__(self):
        return self.name
