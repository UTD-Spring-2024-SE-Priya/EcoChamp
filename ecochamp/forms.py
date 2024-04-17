from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label="Username", required=False)
    email = forms.EmailField(label="Email", required=False)
    password = forms.CharField(label="Password", widget=forms.PasswordInput, required=True)


    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")

        if not (username or email):
            raise forms.ValidationError("Please enter either a username or an email.")

        if username:
            user = authenticate(request=self.request, username=username, password=password)
            if user is None:
                raise forms.ValidationError("Invalid username or password.")

        if email:
            user = authenticate(request=self.request, email=email, password=password)
            if user is None:
                raise forms.ValidationError("Invalid email or password.")

        return cleaned_data