from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

# Create your models here.
class Content(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=timezone.now)
    body = models.TextField(default='')
    url = models.URLField(default='')
    happy = models.BooleanField(default=False)