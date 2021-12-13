from django.urls import path

from . import views

urlpatterns = [
    path("products/create/", views.create_product, name="create-product"),
    path("product/edit/", views.edit_product, name="edit-product"),
    path("product/delete/", views.delete_product, name="delete-product")
]
