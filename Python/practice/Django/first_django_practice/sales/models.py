from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Sale(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField(default=0)
    person = models.ForeignKey("User", on_delete=models.CASCADE)
