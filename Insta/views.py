from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from Insta.models import Post


class HelloWorldView(TemplateView):
    """
    Hello world view for the app.
    """
    template_name = 'test.html'


class PostsView(ListView):
    """
    View for posts
    Model: Post
    Template: index.html
    """
    model = Post
    template_name = "index.html"


class PostDetailView(DetailView):
    """
    Detail view for posts
    Model: Post
    Template: post_detail.html
    """
    model = Post
    template_name = "post_detail.html"
