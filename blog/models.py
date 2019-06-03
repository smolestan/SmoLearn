from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

from lessons.models import Course

# Create your models here.

class Post(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=320)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    comment = models.CharField(max_length=256)

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('comment', kwargs={'pk':self.post.id })
