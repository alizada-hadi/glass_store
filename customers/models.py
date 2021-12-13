from django.db import models
from employees.models import Employee


class Customer(models.Model):
    full_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=14)
    address = models.CharField(max_length=255)

    def __str__(self):
        return f'customer with id {self.id}'
