from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from lessons.models import Course

# Create your models here.

class Event(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    event_date = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=256)
    description = models.TextField()
    invited = models.ManyToManyField(User, blank=True)
    STATUS_CHOICES = (
        ('Upcoming', 'Upcoming'),
        ('Completed', 'Completed'),
    )
    status = models.CharField(max_length=64, choices=STATUS_CHOICES, default='Not available')

