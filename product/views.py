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
    new_order = Order()
    new_order.product = get_object_or_404(Product, pk=id)
    user_id = request.user.id
    user = User.objects.get(id=user_id)
    new_order.user = user
    new_order.save()
    return redirect('order_finished')


def order_list(request):
    orders = Order.objects.all()
    products = Product.objects.all()

    # 해당 유저가 주문한 객체만 orders 에 저장
    orders = orders.filter(user = request.user.id)

    # for 문을 돌면서 이 유저가 가지고 있는 상품 result에 저장 후 return
    result = []

    for i in orders : 
        for j in products : 
            # 상품명으로 비교
            if str(i) == str(j): 
                result.append(j)
                
    return render(request, 'orderlist.html', {'orderlist': result})


def order_finished(request):
    return render(request, 'order_finished.html')