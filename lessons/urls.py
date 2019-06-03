from django.urls import path

from . import views

urlpatterns = [
    path("<int:id>/", views.lesson, name="lesson"),
    path("<int:id>/video/", views.video, name="video"),
    path("<int:id>/presentation/", views.presentation, name="presentation"),
    path("<int:id>/activity/", views.activity, name="activity"),
    path("<int:id>/activity/quiz/", views.get_quiz, name='get_quiz'),
]