from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from accounts.models import Profile
from lessons.models import Lesson

# Create your views here.

@login_required
def index(request):

    try:
        current_course = getattr(request.user.profile.current_course, 'title')
    except:
        current_course = None
    lessons = Lesson.objects.filter(course=request.user.profile.current_course).order_by('chapter', 'number')

    context = {
        "user": request.user,
        "current_course": current_course,
        "lessons": lessons,
    }

    return render(request, "main/index.html", context)