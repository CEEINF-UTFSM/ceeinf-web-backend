from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(blank=True, unique=True)
    password = models.CharField(max_length=256)
    username = models.EmailField(blank=True, unique=True)
