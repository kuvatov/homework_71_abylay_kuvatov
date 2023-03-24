from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect

from .forms import CustomUserCreationForm, CustomUserAuthenticationForm


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


class CustomLoginView(LoginView):
    authentication_form = CustomUserAuthenticationForm
    template_name = 'registration/login.html'
