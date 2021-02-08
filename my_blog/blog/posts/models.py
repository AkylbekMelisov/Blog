from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True,null=True)

    def __str__(self):
        return  self.title

class Post(models.Model):
    blog = models.ForeignKey(Blog,on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title