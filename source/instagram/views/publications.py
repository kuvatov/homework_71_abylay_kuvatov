from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView

from instagram.models import Publication


class PublicationAddView(LoginRequiredMixin, CreateView):
    model = Publication
    template_name = 'publication/publication_add.html'
    fields = ['image', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.likes_count = 0
        form.instance.comments_count = 0
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('publication_detail', kwargs={'pk': self.object.pk})


class PublicationDetailView(DetailView):
    model = Publication
    template_name = 'publication/publication_detail.html'
    context_object_name = 'publication'


class UserSearchView(ListView):
    model = get_user_model()
    template_name = 'user_search.html'
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


class UserDetailView(DetailView):
    model = get_user_model()
    template_name = 'user_detail.html'
    context_object_name = 'user'
