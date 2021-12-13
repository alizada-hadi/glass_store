from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=200)
    quantity = models.DecimalField(decimal_places=5, max_digits=10)

    def __str__(self):
        return self.product_name
