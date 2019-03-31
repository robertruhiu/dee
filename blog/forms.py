from .models import Comment, Post
from django import forms
from taggit.forms import TagField


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')


class PostForm(forms.ModelForm):
    tags = TagField()

    class Meta:
        model = Post
        fields = ('title', 'status', 'body')
