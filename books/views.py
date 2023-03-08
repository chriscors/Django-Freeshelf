from django.contrib.auth.views import LogoutView
from django.shortcuts import render, redirect
from registration import views
from .forms import SearchForm
from .models import Resource, Category, User
import requests


def index(request):
    print(request.user)
    if request.user.is_authenticated:
        return render(request, 'list.html', {"user": request.user})
    else:
        return redirect('/accounts/login', {"user": request.user})


def search(request):
    api_base = 'https://www.googleapis.com/books/v1/volumes?q='

    if request.method == 'POST':
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            params = search_form.cleaned_data
            cleaned_params = {}
            for key, value in params.items():
                if value:
                    cleaned_params[key] = value

            api_params = ""
            for key, value in cleaned_params.items():
                if api_params != "":
                    api_params += "&"
                api_params += f"{key}:{value}"

            print(cleaned_params)

            response = requests.get(
                api_base + api_params)
            print(response)
            print(response.json())
            print(response.url)
            print(len(response.json()))
            responses = response.json()

            results = []
            for result in responses['items']:
                volume_info = result['volumeInfo'],
                results.append(Resource(
                    title=result['volumeInfo']['title'],
                    author=result['volumeInfo']['authors'][0],
                    description=result['volumeInfo']['description'],
                    img_url=result['volumeInfo']['imageLinks']['thumbnail'],
                    url=result['volumeInfo']['infoLink']))
                print(results[-1].__dict__)
            print(results)
            breakpoint()
            return render(request, 'books/search.html',
                          {'form': search_form, 'results': results})

    form = SearchForm()

    return render(request, 'search.html', {'form': form})
