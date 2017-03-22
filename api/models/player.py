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

    def __unicode__(self):
        return self.user.name
