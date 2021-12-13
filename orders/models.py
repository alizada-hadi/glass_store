from django.db import models
from django.utils.translation import deactivate
from employees.models import Employee
from customers.models import Customer
from products.models import Product


class Order(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, null=True, blank=True)
    length = models.DecimalField(decimal_places=4, max_digits=10)
    height = models.DecimalField(decimal_places=4, max_digits=10)
    quantity = models.IntegerField(default=1)
    service_provider = models.ForeignKey(
        Employee, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.customer.full_name}\'s order'


class Bill(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, null=True, blank=True)
    paid = models.DecimalField(decimal_places=4, max_digits=10, default=0)
    remined = models.DecimalField(decimal_places=4, max_digits=10, default=0)
    daily_price = models.DecimalField(
        decimal_places=2, max_digits=10, default=35)
    wasting_percentage = models.DecimalField(
        decimal_places=2, max_digits=4, default=15)
