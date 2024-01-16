from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length = 192)
    sub_title = models.CharField(max_length = 192, default='Test')
    content = models.TextField()
    date = models.DateField(default=timezone.now)