from django.shortcuts import render
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from accounts.models import Profile
from .models import Question, Answer

# Create your views here.

class QuestionListView(LoginRequiredMixin, ListView):
    model = Question
    template_name = 'discussions/discussions.html'
    context_object_name = 'questions'
    ordering = ['-date_posted']
    paginate_by = 5
    
    def get_context_data(self, **kwargs):
        context = super(QuestionListView, self).get_context_data(**kwargs)
        context['current_course'] = self.request.user.profile.current_course
        return context

class QuestionCreateView(LoginRequiredMixin, CreateView):
    model = Question
    fields = ['question']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.course = self.request.user.profile.current_course
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(QuestionCreateView, self).get_context_data(**kwargs)
        context['current_course'] = self.request.user.profile.current_course
        return context

class QuestionUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Question
    fields = ['question']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.course = self.request.user.profile.current_course
        return super().form_valid(form)

    def test_func(self):
        question = self.get_object()
        if self.request.user == question.author:
            return True
        return False

    def get_context_data(self, **kwargs):
        context = super(QuestionUpdateView, self).get_context_data(**kwargs)
        context['current_course'] = self.request.user.profile.current_course
        return context


class QuestionDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Question
    success_url = '/discussions/'

    def test_func(self):
        question = self.get_object()
        if self.request.user == question.author:
            return True
        return False

    def get_context_data(self, **kwargs):
        context = super(QuestionDeleteView, self).get_context_data(**kwargs)
        context['current_course'] = self.request.user.profile.current_course
        return context

class AnswerCreateView(LoginRequiredMixin, CreateView):
    model = Answer
    fields = ['answer']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.course = self.request.user.profile.current_course
        form.instance.question = Question.objects.get(id=(self.request.POST.get('question')))
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(AnswerCreateView, self).get_context_data(**kwargs)
        context['current_course'] = self.request.user.profile.current_course
        question = Question.objects.get(id=self.kwargs['pk'])
        context['current_question'] = question
        context['answers'] = Answer.objects.filter(question=question)
        return context
