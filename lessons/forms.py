from django.forms import ModelForm

from .models import HomeWork

class HomeWorkForm(ModelForm):
    class Meta:
        model = HomeWork
        fields = ('answer', 'attachment', )