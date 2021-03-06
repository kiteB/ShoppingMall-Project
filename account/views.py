from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from .models import User
from django.contrib import auth


def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': '아이디와 비밀번호가 맞지 않습니다.'})
    else:
        return render(request, 'login.html')


def user_signup(request):
    if request.method == "POST":
        if request.POST["password"] == request.POST["password2"]:
            user = User.objects.create_user(
                # 장고 기본 유저 필드
                username = request.POST["username"],
                password = request.POST["password"],

                # 확장 유저 필드
                university = request.POST["university"],
                profile_img = request.FILES.get('profile_img'),

            )
            user.save()
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'signup.html')
    else:
        return render(request, 'signup.html')


def user_logout(request):
    logout(request)
    return redirect('home')


def mypage(request):
    return render(request, 'mypage.html')