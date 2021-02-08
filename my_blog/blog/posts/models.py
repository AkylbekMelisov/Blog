from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True,null=True)

class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)