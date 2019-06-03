from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from accounts.models import Profile
from .models import Event

# Create your views here.

@login_required
def events(request):
    try:
        current_course = request.user.profile.current_course
    except:
        current_course = None

    events = Event.objects.filter(course=current_course)

    context = {
        'current_course': current_course,
        'events': events,
    }
    return render(request, 'events/events.html', context)

@login_required
def event(request, id):
    try:
        current_course = request.user.profile.current_course
    except:
        current_course = None

    event = Event.objects.get(id=id)

    context = {
        'current_course': current_course,
        'event': event,
    }
    return render(request, 'events/event.html', context)