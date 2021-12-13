from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="index"),
    path("", include("products.urls")),
    path("", include("employees.urls")),
    path("", include("customers.urls"))
]
