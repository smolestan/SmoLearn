from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView
from django.contrib.auth.models import User

from accounts.models import Profile
from .models import Post, Comment

# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'blog/blog.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['current_course'] = self.request.user.profile.current_course
        return context

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

    def get_context_data(self, **kwargs):
        context = super(UserPostListView, self).get_context_data(**kwargs)
        context['current_course'] = self.request.user.profile.current_course
        return context

class CommentCreateView(CreateView):
    model = Comment
    fields = ['comment']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.course = self.request.user.profile.current_course
        form.instance.post = Post.objects.get(id=(self.request.POST.get('post')))
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CommentCreateView, self).get_context_data(**kwargs)
        context['current_course'] = self.request.user.profile.current_course
        post = Post.objects.get(id=self.kwargs['pk'])
        context['post'] = post
        context['comments'] = Comment.objects.filter(post=post)
        return context


