from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import DetailView
from django.views.generic.edit import CreateView

from instagram.forms import CommentForm
from instagram.models import Publication


class PublicationCreateView(LoginRequiredMixin, CreateView):
    model = Publication
    template_name = 'publication/publication_create.html'
    fields = ['image', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.likes_count = 0
        form.instance.comments_count = 0
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('publication_detail', kwargs={'pk': self.object.pk})


class PublicationDetailView(LoginRequiredMixin, DetailView):
    model = Publication
    template_name = 'publication/publication_detail.html'
    context_object_name = 'publication'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        likes = self.object.likes.all()
        context['publication_likes'] = likes.values_list('user_id', flat=True)
        context['form'] = CommentForm(instance=self.object)
        return context
