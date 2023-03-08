from django.db import models
from django.contrib.auth.models import AbstractUser
from django.template.defaultfilters import slugify


class Resource(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    description = models.TextField()
    url = models.SlugField(blank=True, null=True, unique=True)
    slug = models.SlugField(default=slugify(title))
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    img_url = models.SlugField(blank=True, null=True)
    category = models.ForeignKey(
        "Category", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(default=slugify(title))


class User(AbstractUser):
    favorite_stories = models.ManyToManyField(Resource)

    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username
