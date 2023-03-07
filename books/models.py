from django.db import models
from django.contrib.auth.models import AbstractUser
from django.template.defaultfilters import slugify


class Resource(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    description = models.TextField()
    url = models.SlugField(default=slugify(title))

    def __str__(self):
        return self.title


class User(AbstractUser):
    favorite_stories = models.ManyToManyField(Resource)

    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username
