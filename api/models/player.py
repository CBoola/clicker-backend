from django.contrib.auth.models import User

from django.db import models
from jsonfield import JSONField


class Player(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    current_state = JSONField(default={})
    structures = JSONField(default={})

    def __str__(self):
        return "{0} {1}".format(self.user.first_name, self.user.last_name)
