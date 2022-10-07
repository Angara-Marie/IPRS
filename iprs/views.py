from django.shortcuts import render
from . import models
from . import forms

# Create your views here.
def register_customer(request):
    if request.method == "POST":
        form = forms.CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = forms.CustomerRegistrationForm()
    return render (request,"wallet/register_customer.html",
    {"form":form})
