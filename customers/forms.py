from django import forms
from django.db import models
from django.http import request
from orders.models import Order
from .models import Customer
from django.forms import inlineformset_factory


class CustomerForm(forms.Form):
    full_name = forms.CharField(max_length=200, required=True)
    phone_number = forms.CharField(max_length=14, required=True)
    address = forms.CharField(max_length=255, required=True)
