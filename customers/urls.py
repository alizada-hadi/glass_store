from django.urls import path
from . import views


urlpatterns = [
    path("customers/all/", views.customer_list, name="customer-list"),
    path("customer/create/", views.create_customer, name="create-customer"),
    path("customer/<str:pk>/detail/",
         views.customer_detail, name="customer-detail"),
    path("customer/<str:pk>/bill/", views.bill_detail, name="bill-detail"),
    path("customer/<str:pk>/update/",
         views.customer_update, name="customer-update"),
    path("custome/<str:pk>/<str:id>/delete/",
         views.delete_customer, name="customer-delete"),
    path("customers/<str:pk>/orders/all/",
         views.customer_orders, name="customer-orders")
]
