from django.contrib import admin
from .models import Course, Lesson, HomeWork, Quiz, QuizQuestion

class LessonAdmin(admin.ModelAdmin):
    list_display = ['course', 'chapter', 'number', 'title', 'status']
    list_editable = ['status']
    list_filter = ['course']

    class Meta:
        model = Lesson

class HomeWorkAdmin(admin.ModelAdmin):
    list_display = ['course', 'lesson', 'author', 'status', 'date_posted']
    list_filter = ['course', 'status']

    class Meta:
        model = HomeWork


# Register your models here.
admin.site.register(Course)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(HomeWork, HomeWorkAdmin)
admin.site.register(Quiz)
admin.site.register(QuizQuestion)
