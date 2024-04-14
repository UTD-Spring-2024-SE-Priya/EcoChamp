# Handles user input

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')
    username = forms.CharField(max_length=150, required=False)

    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')

class LoginForm(forms.Form):
    username_or_email = forms.CharField(label='Username or Email')
    password = forms.CharField(widget=forms.PasswordInput)
