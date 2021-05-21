from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField('title', max_length=20)
    content = models.CharField('content', max_length=200)
