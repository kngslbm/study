from django.db import models


class Sale(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField(default=0)
    person = models.ForeignKey("Person", on_delete=models.CASCADE)


class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField(default=0)
