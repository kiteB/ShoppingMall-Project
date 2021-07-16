from django.shortcuts import render, redirect, get_object_or_404
from account.models import User
from django.utils import timezone
from product.models import Product
from .models import *


def create(request):
    if request.method == "POST":
        new_product = Product()
        new_product.product_name = request.POST['product_name']
        new_product.explanation = request.POST['explanation']
        new_product.price = request.POST['price']
        new_product.image = request.FILES.get('image')

        new_product.save()
        return redirect('home')
    else:
        return render(request, 'new.html')


def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})


def detail(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, 'detail.html', {'product': product})


def edit(request, id):
    if request.method == "POST":
        edit_product = Product.objects.get(pk=id)
        edit_product.product_name = request.POST['product_name']
        edit_product.explanation = request.POST['explanation']
        edit_product.price = request.POST['price']
        edit_product.image = request.FILES.get('image')
        edit_product.save()
        return redirect('detail', edit_product.id)
    else:
        product = Product.objects.get(pk=id)
        return render(request, 'edit.html', {'product': product})


def delete(request, id):
    delete_product = Product.objects.get(pk=id)
    delete_product.delete()
    return redirect('home')