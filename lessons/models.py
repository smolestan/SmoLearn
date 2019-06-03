from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=128)
    image = models.ImageField(default='default.png', upload_to='courses_pics')
    assigned_to = models.ManyToManyField(User)

    def __str__(self):
        return self.title

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    chapter = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(100)])
    number = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(100)])
    title = models.CharField(max_length=256)
    STATUS_CHOICES = (
        ('Not available', 'Not available'),
        ('Available', 'Available'),
    )
    status = models.CharField(max_length=64, choices=STATUS_CHOICES, default='Not available')
    lesson_video = models.FileField(upload_to='lesson_vids', blank=True, null=True)
    lesson_file = models.FileField(upload_to='lesson_files', blank=True, null=True)
    task = models.TextField(blank=True, null=True)
    attachment = models.FileField(upload_to='lesson_att', blank=True, null=True)

    def __str__(self):
        return self.title

class HomeWork(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    answer = models.TextField()
    attachment = models.FileField(upload_to='homework_att', blank=True, null=True)
    STATUS_CHOICES = (
        ('Processing', 'Processing'),
        ('Rejected', 'Rejected'),
        ('Done', 'Done'),
    )
    status = models.CharField(max_length=64, choices=STATUS_CHOICES, default='Not available')
    comment = models.TextField(blank=True, null=True)

class Quiz(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

class QuizQuestion(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_content = models.CharField(max_length=64)
    QUIZ_ANSWERS = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    quiz_correct_answer = models.CharField(max_length=64, choices=QUIZ_ANSWERS)