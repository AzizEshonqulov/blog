from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=100)
    view_count = models.IntegerField(null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self) -> str:
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    comment = models.CharField(max_length=500)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True, related_name='comments')

    def __str__(self) -> str:
        return self.comment