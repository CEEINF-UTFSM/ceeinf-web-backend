from django.db import models


class Post(models.Model):
    title        = models.CharField(max_length=100)
    content      = models.TextField()
    published_on = models.DateTimeField(auto_now=True)
