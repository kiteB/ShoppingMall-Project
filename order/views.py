from django.shortcuts import render, redirect, get_object_or_404
from account.models import User
from product.models import Product
from .models import *


def create_order(request, product_id):
    if request.method == 'POST':
        order = Product()
        order.product_name = get_object_or_404(Product, pk=product_id)

        user_id = request.user.id
        user = User.objects.get(id=user_id)
        order.user = user
        order.save()
        return redirect('orderlist')