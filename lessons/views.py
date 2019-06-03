from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import JsonResponse

from accounts.models import Profile
from .models import Course, Lesson, HomeWork, Quiz, QuizQuestion
from main.models import MainImgs
from .forms import HomeWorkForm

# Create your views here.

@login_required
def lesson(request, id):
    try:
        current_course = getattr(request.user.profile.current_course, 'title')
    except:
        current_course = None
    
    requested_lesson = Lesson.objects.get(id=id)

    if requested_lesson.course.title == str(current_course): 
        lesson = requested_lesson
    else:
        lesson = None

    videoicon = MainImgs.objects.get(title='VideoLesson')
    fileicon = MainImgs.objects.get(title='Presentation')
    activityicon = MainImgs.objects.get(title='Activity')

    context = {
        'current_course': current_course,
        'lesson': lesson,
        'videoicon': videoicon,
        'fileicon': fileicon,
        'activityicon': activityicon,
    }

    return render(request, 'lessons/lesson.html', context)

@login_required
def video(request, id):
    try:
        current_course = getattr(request.user.profile.current_course, 'title')
    except:
        current_course = None
    
    requested_lesson = Lesson.objects.get(id=id)

    if requested_lesson.course.title == str(current_course): 
        lesson = requested_lesson
    else:
        lesson = None

    context = {
        'current_course': current_course,
        'lesson': lesson,
    }

    return render(request, 'lessons/video.html', context)

@login_required
def presentation(request, id):
    try:
        current_course = getattr(request.user.profile.current_course, 'title')
    except:
        current_course = None
    
    requested_lesson = Lesson.objects.get(id=id)

    if requested_lesson.course.title == str(current_course): 
        lesson = requested_lesson
    else:
        lesson = None

    context = {
        'current_course': current_course,
        'lesson': lesson,
    }

    return render(request, 'lessons/file.html', context)

@login_required
def activity(request, id):
    form = None
    status = None
    try:
        current_course = getattr(request.user.profile.current_course, 'title')
    except:
        current_course = None
    
    requested_lesson = Lesson.objects.get(id=id)

    if requested_lesson.course.title == str(current_course): 
        lesson = requested_lesson
    else:
        lesson = None

    course = Course.objects.get(title=current_course)
    author = request.user

    try: 
        homework = HomeWork.objects.get(course=course, lesson=lesson, author=author)
        status = homework.status
        if homework.status == 'Rejected':
            sent = False
            rejected = True
        else:
            sent = True
            rejected = False
    except:
        sent = False
        rejected = False
        form = HomeWorkForm()

    if request.method == "POST" and rejected:
        homework.status = 'Processing'
        homework.comment = ''
        homework.save()
        form = HomeWorkForm(request.POST, request.FILES, instance=homework)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your HomeWork has been updated!')
            return redirect('activity', lesson.id)        


    if request.method == "POST" and not sent:
        status = 'Processing'
        homework = HomeWork.objects.create(course=course, lesson=lesson, author=author, status=status)
        form = HomeWorkForm(request.POST, request.FILES, instance=homework)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your HomeWork has been sent!')
            return redirect('activity', lesson.id)        

    if sent or rejected:
        comment = homework.comment
        if rejected:
            form = HomeWorkForm()
    else:
        comment = None

    smiles = MainImgs.objects.filter(title__in=["VeryBad", "Bad", "Normal", "Good", "VeryGood"])

    context = {
        'current_course': current_course,
        'lesson': lesson,
        'form': form,
        'status': status,
        'comment': comment,
        'smiles': smiles,
    }

    return render(request, 'lessons/activity.html', context)
    
def get_quiz(request, id):
    quiz = Quiz.objects.get(lesson=id)
    questions = QuizQuestion.objects.filter(quiz=quiz)
    questions_serialized = serializers.serialize('json', questions, fields = ['question_content', 'quiz_correct_answer'])
    return JsonResponse(questions_serialized, safe=False)