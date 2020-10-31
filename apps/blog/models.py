from django.db import models

from apps.users.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_on = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
