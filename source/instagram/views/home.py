from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from instagram.models import Publication


class HomeView(LoginRequiredMixin, ListView):
    model = Publication
    template_name = 'home.html'
    context_object_name = 'publications'

    # def get_queryset(self):
    #     subscriptions = self.request.user.subscriptions.all()
    #     subscribed_to_users = [subscription.subscribed_to for subscription in subscriptions]
    #     publications = Publication.objects.filter(user__in=subscribed_to_users).order_by('-created_at')
    #     return publications

    def get_queryset(self):
        subscriptions = self.request.user.subscriptions.all()
        subscribed_to_users = [subscription.subscribed_to for subscription in subscriptions]
        publications = Publication.objects.filter(user__in=subscribed_to_users).order_by('-created_at')
        return publications
