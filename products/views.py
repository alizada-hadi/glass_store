from django.shortcuts import redirect, render

import products
from .models import Product


def create_product(request):
    if request.method == "POST":
        pro_name = request.POST.get("product_name")
        pro_quantity = request.POST.get("product_quantity")
        Product.objects.create(
            product_name=pro_name,
            quantity=pro_quantity
        )
        return redirect("/")
    return render(request, "products/form.html")


def edit_product(request):
    pk = request.POST.get("product_id")
    product = Product.objects.get(pk=pk)
    pro_name = request.POST.get("product_name")
    pro_quantity = request.POST.get("product_quantity")
    if request.method == "POST":
        product.product_name = pro_name
        product.quantity = pro_quantity
        product.save()
    return redirect("/")


def delete_product(request):
    pk = request.POST.get("product_pk")
    product = Product.objects.get(pk=pk)
    print(f"my product is {product}")
    if request.method == "POST":
        product.delete()
    return redirect("/")
