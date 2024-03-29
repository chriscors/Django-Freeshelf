from django.db import models
from django.contrib.auth.models import AbstractUser
from django.template.defaultfilters import slugify
from django.urls import reverse


class Resource(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    description = models.TextField()
    url = models.CharField(max_length=400, blank=True, null=True, unique=False)
    slug = models.SlugField(null=True, unique=True)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    img_url = models.TextField(blank=True, null=True)
    category = models.ForeignKey(
        "Category", on_delete=models.CASCADE, null=True, blank=True)
    api_id = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        ordering = ['-created_at']


class Category(models.Model):
    type = models.CharField(max_length=150)
    slug = models.SlugField(null=True, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.type)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.type


class User(AbstractUser):
    favorite_stories = models.ManyToManyField(Resource, related_name="users")

    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username
