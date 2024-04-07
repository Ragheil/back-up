from django.contrib.auth.models import User
from django.db import models


class Registration(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return()


class Post(models.Model):
    user_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=2000)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['complete']
   
