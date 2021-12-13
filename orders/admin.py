from django.contrib import admin

from .models import Order, Bill

admin.site.register(Order)
admin.site.register(Bill)
