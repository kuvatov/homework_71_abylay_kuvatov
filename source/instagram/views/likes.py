from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy

from instagram.models import Like, Publication


class LikeView(LoginRequiredMixin, CreateView):
    model = Like
    fields = []

    def form_valid(self, form):
        publication_id = self.kwargs['pk']
        publication = Publication.objects.get(id=publication_id)
        if not Like.objects.filter(publication=publication, user=self.request.user).exists():
            like = form.save(commit=False)
            like.user = self.request.user
            like.publication = publication
            like.save()
            publication.likes_count += 1
            publication.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('publication_detail', args=(self.kwargs['pk'],))


class UnlikeView(LoginRequiredMixin, DeleteView):
    model = Like

    def delete(self, request, *args, **kwargs):
        like = self.get_object()
        publication = like.publication
        if like.user == request.user:
            publication.likes_count -= 1
            publication.save()
            return super().delete(request, *args, **kwargs)
        return HttpResponseForbidden()

    def get_success_url(self):
        return reverse_lazy('publication_detail', args=(self.object.publication.id,))
