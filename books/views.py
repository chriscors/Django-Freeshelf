from django.contrib.auth.views import LogoutView
from django.shortcuts import render, redirect
from registration import views
from .forms import SearchForm, SortForm, EditBookForm
from .models import Resource, Category, User
import requests
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


@login_required
def index(request):
    print(request.user)
    return render(request, 'list.html',
                  {"user": request.user, 'books': Resource.objects.all(),
                   'sort_form': SortForm()})


@login_required
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

            responses = response.json()

            results = []
            for result in responses['items']:
                print(result['volumeInfo'])
                results.append(Resource(
                    title=result['volumeInfo']['title'],
                    url=result['volumeInfo']['infoLink'],
                    api_id=result['id'],))
                try:
                    print({result['volumeInfo']['authors'][0]})
                    results[-1].author = ", ".join(
                        result['volumeInfo']['authors'])
                    print(f'AUTHOR ASSIGN: {results[-1].author}\n')
                except:
                    print("description unavailable")

                try:
                    results[-1].description = result['volumeInfo']['description']
                except:
                    print("author unavailable\n")

                try:
                    results[-1].img_url = result['volumeInfo']['imageLinks']['thumbnail']
                except:
                    print("image unavailable")

                try:
                    category = Category(
                        type=result['volumeInfo']['categories'][0])
                    # category = Category.objects.get_or_create(
                    #     type=result['volumeInfo']['categories'][0])
                    print(category)
                    print(category.type)
                    results[-1].category = category
                except:
                    print("category unavailable")

                print(results[-1].__dict__)
            print(results)

            return render(request, 'search.html',
                          {'form': search_form, 'results': results})

    form = SearchForm()

    return render(request, 'search.html', {'form': form})


@ login_required
def resource_add(request, api_id):
    api_base = 'https://www.googleapis.com/books/v1/volumes?q='+api_id

    api_params = ""

    response = requests.get(api_base)
    print(response)
    result = response.json()
    print(response.url)
    result = result['items'][0]
    book = Resource(title=result['volumeInfo']['title'],
                    url=result['volumeInfo']['infoLink'],
                    api_id=result['id'],)

    try:
        print(result['volumeInfo']['authors'][0])
        book.author = ", ".join(result['volumeInfo']['authors'])
        print(f'AUTHOR ASSIGN: {book.author}\n')
    except:
        print("description unavailable")

    try:
        book.description = result['volumeInfo']['description']
    except:
        print("description unavailable")

    try:
        book.img_url = result['volumeInfo']['imageLinks']['thumbnail']
    except:
        print("image unavailable")

    try:
        category = Category.objects.get_or_create(
            type=result['volumeInfo']['categories'][0])

        category.save()
        book.category = category
    except:
        print("category unavailable")
    book.save()

    edit_form = EditBookForm(instance=book)

    return render(request, 'edit.html',
                  {'form': edit_form, 'book': book})


@ login_required
def resource_details(request, slug):
    book = get_object_or_404(Resource, slug=slug)
    return render(request, 'details.html', {'book': book})


@ login_required
def resource_delete(request, slug):
    book = get_object_or_404(Resource, slug=slug)
    book.delete()
    return redirect('index')


@ login_required
def resource_edit(request, slug):
    book = get_object_or_404(Resource, slug=slug)
    print(book.__dict__)
    print(book)
    if request.method == 'POST':
        # print(book.__dict__)
        form = EditBookForm(request.POST, initial=book.__dict__)

        if form.is_valid():
            book.title = form.cleaned_data['title']
            book.author = form.cleaned_data['author']
            book.category = form.cleaned_data['category']

            book.description = form.cleaned_data['description']

            book.url = form.cleaned_data['url']
            book.save()

            return redirect('resource_details', slug=book.slug)
        print(form.errors)

    edit_form = EditBookForm(instance=book)

    return render(request, 'edit.html',
                  {'form': edit_form, 'book': book})


@ login_required
def favorite(request, pk):

    resource = get_object_or_404(Resource, pk=pk)

    request.user.favorite_stories.add(resource)

    return redirect('index')


@ login_required
def unfavorite(request, pk):
    resource = get_object_or_404(Resource, pk=pk)

    request.user.favorite_stories.remove(resource)

    return redirect('index')
