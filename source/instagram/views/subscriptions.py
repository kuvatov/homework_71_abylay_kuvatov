from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView

from instagram.models import Subscription


class SubscriptionCreateView(LoginRequiredMixin, CreateView):
    model = Subscription
    fields = []
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        subscribed_to = get_object_or_404(get_user_model(), pk=self.kwargs.get('pk'))
        subscription = form.save(commit=False)
        subscription.subscriber = self.request.user
        subscription.subscribed_to = subscribed_to
        subscription.save()
        subscribed_to.subscribers_count += 1
        subscribed_to.save()
        self.request.user.subscriptions_count += 1
        self.request.user.save()
        return super().form_valid(form)


class SubscriptionDeleteView(LoginRequiredMixin, DeleteView):
    model = Subscription
    success_url = reverse_lazy('home')

    def delete(self, request, *args, **kwargs):
        subscription = self.get_object()
        subscribed_to = subscription.subscribed_to
        subscription.delete()
        subscribed_to.subscribers_count -= 1
        subscribed_to.save()
        self.request.user.subscriptions_count -= 1
        self.request.user.save()
        return super().delete(request, *args, **kwargs)
