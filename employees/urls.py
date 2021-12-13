from django.urls import path

from . import views


urlpatterns = [
    path("create/employees/", views.create_employee, name="create-employee")
]
