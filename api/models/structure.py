from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Structure(models.Model):

    name = models.CharField(max_length=25)
    description = models.CharField(max_length=100)
    icon = models.ImageField(upload_to="structures")

    base_prize = models.IntegerField(
        default=1,
        validators=[MinValueValidator(1)])
    production_rate = models.IntegerField(
        default=1,
        validators=[MinValueValidator(1)])

    class Meta:
        ordering = ['base_prize']

    def __str__(self):
        return self.name
