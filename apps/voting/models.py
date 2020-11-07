from django.db import models
from .validators import validate_length


class Poll(models.Model):
    state = models.CharField(max_length=256)
    begin_time = models.DateTimeField()
    end_time = models.DateTimeField()
    name = models.CharField(max_length=512)


class Vote(models.Model):
    option = models.CharField(max_length=512)
    sign = models.CharField(max_length=64, validators=[validate_length])
    poll = models.ForeignKey(Poll, on_delete=models.RESTRICT)
