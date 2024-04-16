from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def __str__(self):
        return self.username


class Sale(models.Model):
    stuff = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    content = models.TextField(max_length=500)
    saller = models.ForeignKey("User", on_delete=models.CASCADE)
