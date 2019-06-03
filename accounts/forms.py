from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from .models import Customer, Profile

class LoginForm(forms.Form):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': _('Username')}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': _('Password')}))

    def clean_username(self):
        username = self.cleaned_data.get("username")
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise forms.ValidationError(_("Invalid Username"))
        return username
    
    def clean_password(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        try:
            user = User.objects.get(username=username)
        except:
            user = None
        if user is not None and not user.check_password(password):
            raise forms.ValidationError(_("Invalid Password"))
        elif user is None:
            pass
        else:
            return password

class ContactForm(forms.Form):
    first_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': _('First Name'), 'class': 'form-control'}))
    last_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': _('Last Name'), 'class': 'form-control'}))
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'placeholder': _('Email'), 'class': 'form-control'}))
    phone = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': _('Phone Number'), 'class': 'form-control'}))
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        user_count = Customer.objects.filter(email=email).count()
        if user_count > 0 :
            raise forms.ValidationError(_("This email has already been registered"))
        return email

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']