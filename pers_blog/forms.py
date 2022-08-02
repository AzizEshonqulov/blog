from dataclasses import fields
from django import forms
from pers_blog.models import Post, Comment


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category', 'image']

class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment', 'post']