from django.contrib.auth.views import LogoutView
from django.shortcuts import render, redirect
from registration import views
import requests


def index(request):
    print(request.user)
    if request.user.is_authenticated:
        return render(request, 'list.html', {"user": request.user})
    else:
        return redirect('/accounts/login', {"user": request.user})


def search(request, **params):
    api_base = 'https://www.googleapis.com/books/v1/volumes?q='

    response = requests.get(api_base, params)
