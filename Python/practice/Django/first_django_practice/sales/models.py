from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Sale(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stuff = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    content = models.TextField(max_length=500)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
