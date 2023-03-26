from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import EmailField


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2', 'avatar', 'name', 'user_information',
                  'phone_number', 'sex')


class CustomUserAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='Логин или Email')
