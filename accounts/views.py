from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext as _

from .models import Customer
from accounts.models import Profile
from lessons.models import Course
from .forms import LoginForm, ContactForm, UserUpdateForm, ProfileUpdateForm

# Create your views here.

def login_view(request):

    valuenext = request.POST.get('next')
    login_form = LoginForm(request.POST or None)
    contact_form = ContactForm(request.POST or None)

    context = {
        "login_form": login_form,
        "contact_form": contact_form,
    }

    if request.method == "POST":
        if request.POST.get('submit') == 'sign_in':
            if login_form.is_valid():
                username = login_form.cleaned_data["username"]
                password = login_form.cleaned_data["password"]
                user = authenticate(request, username=username, password=password)
                login(request, user)
                if valuenext:
                    return redirect(valuenext)
                else:
                    return HttpResponseRedirect(reverse("index"))
            else:
                return render(request, "accounts/login.html", context)
        elif request.POST.get('submit_reg_form') == 'contact':
            if contact_form.is_valid():
                customer = Customer.objects.create()
                customer.first_name = contact_form.cleaned_data["first_name"]
                customer.last_name = contact_form.cleaned_data["last_name"]
                customer.email = contact_form.cleaned_data["email"]
                customer.phone = contact_form.cleaned_data["phone"]
                customer.status = "NEW"
                customer.save()
                contact_message = _("Success! Please wait for a call or email from our customer manager.")
                return render(request, "accounts/login.html", {"contact_message": contact_message, "login_form": login_form, "contact_form": contact_form})
            else:
                return render(request, "accounts/login.html", context)
    else:
        return render(request,"accounts/login.html", context)    

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))

@login_required
def profile(request):
    if request.method == "POST":
        if request.POST.get('submit') == 'update_profile':
            u_form = UserUpdateForm(request.POST, instance=request.user)
            p_form = ProfileUpdateForm( request.POST,
                                        request.FILES, 
                                        instance=request.user.profile)
            if u_form.is_valid() and p_form.is_valid():
                u_form.save()
                p_form.save()
                messages.success(request, f'Your account has been updated!')
                return redirect('profile')
        else:
            u_form = UserUpdateForm(instance=request.user)
            p_form = ProfileUpdateForm(instance=request.user.profile)
            new_course_id = request.POST.get('course')
            new_course = Course.objects.get(id=new_course_id)
            if request.user.course_set.filter(id=new_course_id).exists():
                profile = Profile.objects.get(user=request.user)
                profile.current_course = new_course
                profile.save()
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    assigned_courses = Course.objects.filter(assigned_to=request.user)
    try:
        current_course = getattr(request.user.profile.current_course, 'title')
    except:
        current_course = None

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'assigned_courses': assigned_courses,
        'current_course': current_course,
    }
    return render(request, 'accounts/profile.html', context)