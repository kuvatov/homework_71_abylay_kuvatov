from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from .forms import CustomUserCreationForm, CustomUserAuthenticationForm


class CustomRegisterView(CreateView):
    model = get_user_model()
    form_class = CustomUserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('home')


class CustomLoginView(LoginView):
    authentication_form = CustomUserAuthenticationForm
    template_name = 'registration/login.html'


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "profile.html"
