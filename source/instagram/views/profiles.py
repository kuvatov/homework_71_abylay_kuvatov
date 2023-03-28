from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, UpdateView

from instagram.models import Subscription
from users.forms import CustomUserCreationForm


class ProfileSearchView(ListView):
    model = get_user_model()
    template_name = 'profile/user_profile_search.html'
    context_object_name = 'users'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(username__icontains=query) |
                Q(email__icontains=query) |
                Q(name__icontains=query)
            ).distinct()
        return queryset


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = get_user_model()
    template_name = 'profile/user_profile.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        subscription = Subscription.objects.filter(subscriber=self.request.user, subscribed_to=user).first()
        context['subscription'] = subscription
        return context


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "profile/personal_profile.html"


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = CustomUserCreationForm
    template_name = 'profile/personal_profile_update.html'
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        return self.request.user
