from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from Insta.models import Post
from django.urls import reverse_lazy
from Insta.forms import CustomUserCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin


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


class PostCreateView(LoginRequiredMixin, CreateView):
    """
    Required Login, provided by LoginRequiredMixin
    View for creating posts, user will provide Post.id nad POst.inmage
    Model: post
    Template: 'post_create.html'
    """
    model = Post
    # html page name
    template_name = 'post_create.html'
    # user will provide all fields for Model Post
    fields = '__all__'
    # redirect to login page if not logged in
    login_url = 'login'


class PostUpdateView(UpdateView):
    """
    View for updating posts, only providing title to be updated
    Model: post
    Template: 'post_update.html'
    """
    model = Post
    template_name = 'post_update.html'
    fields = ['title']


class PostDeleteView(DeleteView):

    model = Post
    template_name = 'post_delete.html'
    # reverse_lazy for deletion, cannot use reverse to redirection during deletion
    success_url = reverse_lazy("posts")


class SignUp(CreateView):
    form_class = CustomUserCreateForm
    template_name = 'signup.html'
    success_url = reverse_lazy("login")
