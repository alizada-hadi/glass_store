from django.db import models
from django.db.models.base import Model


class Employee(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=14, unique=True)
    address = models.CharField(max_length=255)
    salary = models.IntegerField(default=0)

    def __str__(self):
        return self.name
