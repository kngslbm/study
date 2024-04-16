from django.db import models


class Sale(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField(default=0)
