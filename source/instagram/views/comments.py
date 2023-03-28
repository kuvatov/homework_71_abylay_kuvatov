from django.urls import reverse_lazy
from django.views.generic import CreateView

from instagram.models import Comment, Publication


class CommentCreateView(CreateView):
    model = Comment
    fields = ['text']

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.publication = Publication.objects.get(pk=self.kwargs['pk'])
        publication = form.instance.publication
        publication.comments_count = Comment.objects.filter(publication=publication).count()
        publication.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('publication_detail', args=(self.kwargs['pk'],))
