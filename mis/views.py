from django.shortcuts import render
from products.models import Product
from employees.models import Employee


def index(request):
    products = Product.objects.all()
    employees = Employee.objects.all()
    context = {
        "products": products,
        "employees": employees
    }
    return render(request, "dashboard/index.html", context)
