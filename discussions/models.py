from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

from lessons.models import Course


# Create your models here.

class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    question = models.CharField(max_length=256)

    def __str__(self):
        return self.question

    def get_absolute_url(self):
        return reverse('discussions')

class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    answer = models.CharField(max_length=256)

    def __str__(self):
        return self.answer

    def get_absolute_url(self):
        return reverse('answer', kwargs={'pk':self.question.id })
