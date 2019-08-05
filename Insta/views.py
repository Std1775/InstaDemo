from django.shortcuts import render
from annoying.decorators import ajax_request
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from Insta.models import Post, Like, InstaUser, UserConnection
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

    # problematic method, need fix
    # def get_queryset(self):
    #     current_user = self.request.user
    #     following = set()
    #     for conn in UserConnection.objects.filter(creator=current_user).select_related('following'):
    #         following.add(conn.following)
    #     return Post.objects.filter(author__in=following)


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


# function based view to respond ajax request
@ajax_request
def addLike(request):
    post_pk = request.POST.get('post_pk')
    post = Post.objects.get(pk=post_pk)
    try:
        like = Like(post=post, user=request.user)
        # save function may fail since we have defined unique_together in Like Model(models.py)
        like.save()
        result = 1
    except Exception as e:
        like = Like.objects.get(post=post, user=request.user)
        like.delete()
        result = 0

    return {
        'result': result,
        'post_pk': post_pk
    }


class UserDetailView(DetailView):
    model = InstaUser
    template_name = 'user_detail.html'

