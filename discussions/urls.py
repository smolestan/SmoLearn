from django.urls import path
from .views import (
    QuestionListView, 
    QuestionCreateView,
    QuestionUpdateView,
    QuestionDeleteView,
    AnswerCreateView,
)

from . import views

urlpatterns = [
    path("", QuestionListView.as_view(), name="discussions"),
    path("<int:pk>/update/", QuestionUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", QuestionDeleteView.as_view(), name="delete"),
    path("new/", QuestionCreateView.as_view(), name="create"),
    path("<int:pk>/", AnswerCreateView.as_view(), name="answer"),
]