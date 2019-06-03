from django.urls import path
from .views import PostListView, CommentCreateView, UserPostListView

from . import views

urlpatterns = [
    path("", PostListView.as_view(), name="blog"),
    path("<int:pk>/", CommentCreateView.as_view(), name='comment'),
    path("user/<str:username>", UserPostListView.as_view(), name="user-posts"),
]