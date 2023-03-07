from django.shortcuts import render, redirect


def index(request):
    print(request.user)
    if request.user.is_authenticated:
        return render(request, 'list.html')
    else:
        return redirect('/accounts/login')
