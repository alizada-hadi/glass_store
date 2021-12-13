from django.utils import timezone
from django.forms import inlineformset_factory
from django.shortcuts import redirect, render
from customers.models import Customer
from orders.models import Bill, Order
from .forms import CustomerForm


def customer_list(request):
    customers = Customer.objects.all()

    context = {
        "customers": customers
    }

    return render(request, "customers/list.html", context)


def create_customer(request):
    if request.method == "POST":
        full_name = request.POST.get("customer_name")
        phone = request.POST.get("customer_phone")
        address = request.POST.get("customer_address")

        customer = Customer.objects.create(
            full_name=full_name,
            phone_number=phone,
            address=address
        )
        return redirect("customer-detail", customer.pk)

    return render(request, "customers/form.html")


def customer_detail(request, pk):
    if pk:
        customer = Customer.objects.get(pk=pk)
    else:
        customer = Customer()
    if request.method == "POST":
        name = request.POST.get("customer_name")
        phone = request.POST.get("customer_phone")
        address = request.POST.get("customer_address")
    OrderInlineFromSet = inlineformset_factory(
        Customer, Order, fields=("product", "length", 'height', 'quantity', 'service_provider',), extra=6, can_delete=True)
    formset = OrderInlineFromSet(instance=customer)
    if request.method == "POST":
        formset = OrderInlineFromSet(request.POST or None, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect("bill-detail", customer.pk)
    context = {"formset": formset}
    return render(request, "customers/detail.html", context)


def bill_detail(request, pk):
    today = timezone.now().date()
    customer = Customer.objects.get(pk=pk)
    orders = customer.order_set.all()
    calculations = []
    bill = Bill.objects.last()
    if request.method == "POST":
        price = request.POST.get("price_day")
        percentage = request.POST.get("west_percentage")
        paid = request.POST.get("paid_amount")
        bill.daily_price = price
        bill.wasting_percentage = percentage
        bill.paid = paid
        bill.save()

    total = 0

    paid_amount = 0
    remind_amount = 0
    foot_total_amount = 0

    d_percentage = float(bill.wasting_percentage)
    d_price = float(bill.daily_price)
    for calc in customer.order_set.all():
        width = calc.length
        height = calc.height
        size = float(width * height)
        foot = size / 900
        quantity = calc.quantity
        find_per = float((d_percentage * foot) / 100)

        total_of_percentage = foot + find_per
        foot_total_amount += total_of_percentage * quantity
        total_price = total_of_percentage * quantity * d_price
        calculations.append({"size_cm": size, 'size_ft': foot,
                            "total_of_percentage": total_of_percentage, 'quantity': quantity, 'd_price': d_price,  "total_price": total_price})

    for i in calculations:
        total += i['total_price']
    paid_amount = float(bill.paid)
    remind_amount = total - paid_amount
    context = {
        "orders": orders,
        "customer": customer,
        "bill": bill,
        "calculations": calculations,
        "total": total,
        "today": today,
        "paid_amount": paid_amount,
        "remind_amount": remind_amount,
        "foot_total_amount": foot_total_amount
    }
    return render(request, "customers/bill.html", context)


def customer_orders(request, pk):

    customer = Customer.objects.get(pk=pk)
    bill = Bill.objects.last()
    today_orders = []
    total = 0

    paid_amount = 0
    remind_amount = 0

    d_percentage = float(bill.wasting_percentage)
    d_price = float(bill.daily_price)
    for calc in customer.order_set.all():
        width = calc.length
        height = calc.height
        size = int(width * height)
        foot = size / 900
        quantity = calc.quantity
        find_per = int((d_percentage * size/900) / 100)
        total_of_percentage = foot + find_per
        total_price = total_of_percentage * quantity * d_price
        today_orders.append({"id": calc.id, 'length': calc.length,
                            "height": calc.height,
                             "total_of_percentage": total_of_percentage, 'quantity': quantity, 'd_price': d_price,
                             "paid": bill.paid,
                             "total_price": total_price})
    for t in today_orders:
        total += t['total_price']

    context = {
        "customer": customer,
        "today_orders": today_orders,
        "total": total
    }
    return render(request, "customers/orders.html", context)


def customer_update(request, pk):
    customer = Customer.objects.get(pk=pk)
    if request.method == "POST":
        name = request.POST.get("customer_name")
        phone = request.POST.get("customer_phone")
        address = request.POST.get("customer_address")
        customer.full_name = name
        customer.phone_number = phone
        customer.address = address
        customer.save()

    return redirect("bill-detail", customer.pk)


def delete_customer(request, pk, id):
    customer = Customer.objects.get(pk=pk)
    bill = Bill.objects.get(pk=id)

    if request.method == "POST":
        customer.delete()
        bill.delete()
    return redirect("/")
