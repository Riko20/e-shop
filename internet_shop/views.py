from django.shortcuts import render, redirect, reverse
from products.models import Product
from .forms import SubscriberForm
from .models import Subscriber
from django.http import HttpResponse

# Create your views here.

def home(request):
    # msg = "Good day everybody. We will open soon."
    # return render(request, 'internet_shop/home_template.html', context=msg)
    products = Product.objects.all()
    subscr = Subscriber()
    form = SubscriberForm()
    if request.method == "POST":
        form = SubscriberForm(request.POST, instance=subscr)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'internet_shop/home_template.html', context={'forma':form, 'products': products})

