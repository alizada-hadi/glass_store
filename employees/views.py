from django.shortcuts import redirect, render
from .models import Employee


def create_employee(request):
    if request.method == "POST":
        emp_name = request.POST.get("emp_name")
        emp_phone = request.POST.get("emp_phone")
        emp_address = request.POST.get("emp_address")
        emp_salary = request.POST.get("emp_salary")

        Employee.objects.create(
            name=emp_name,
            phone=emp_phone,
            address=emp_address,
            salary=emp_salary
        )
        return redirect("/")
