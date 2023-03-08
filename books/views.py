from django.contrib.auth.views import LogoutView
from django.shortcuts import render, redirect
from registration import views


def index(request):
    print(request.user)
    if request.user.is_authenticated:
        return render(request, 'list.html', {"user": request.user})
    else:
        return redirect('/accounts/login', {"user": request.user})
