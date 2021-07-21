from django.shortcuts import render, redirect, get_object_or_404
from account.models import User
from django.utils import timezone
from product.models import Product
# from django.core import paginator
from django.core.paginator import Paginator
from .models import *
from order.models import Order


def home(request):
    products = Product.objects.all()
    paginator = Paginator(products, 3)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'home.html', {'products': page})


def create(request):
    if request.method == "POST":
        new_product = Product()
        new_product.product_name = request.POST['product_name']
        new_product.explanation = request.POST['explanation']
        new_product.price = request.POST['price']
        new_product.image = request.FILES.get('image')

        user_id = request.user.id
        user = User.objects.get(id=user_id)
        new_product.user = user
        new_product.save()
        return redirect('home')
    else:
        return render(request, 'new.html')


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


''' Order '''
def create_order(request, id):
    if request.method == 'GET':
        order = Order()
        order.product = get_object_or_404(Product, pk=id)

        user_id = request.user.id
        user = User.objects.get(id=user_id)
        order.user = user
        order.save()
        # return redirect('home')
        return render(request, 'orderlist.html', {'orderlist': order})