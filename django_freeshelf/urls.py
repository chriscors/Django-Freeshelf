"""django_freeshelf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from books import views
# from registration.backends.default import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.backends.simple.urls')),
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('added/<str:api_id>', views.resource_add, name='resource_add'),
    path('resource/<int:pk>/favorite', views.favorite,
         name='resource_favorite'),
    path('resource/<int:pk>/unfavorite', views.unfavorite,
         name='resource_unfavorite'),
    path('<slug:slug>/edit', views.resource_edit, name='resource_edit'),
    path('<slug:slug>', views.resource_details, name='resource_details'),
    path('<slug:slug>/delete', views.resource_delete, name='resource_delete'),
]
