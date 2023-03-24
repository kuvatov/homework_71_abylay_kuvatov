from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy

from instagram.models import Comment, Publication


class CommentCreateView(CreateView):
    model = Comment
    fields = ['text']
    template_name = 'comment/comment_add.html'
    success_url = reverse_lazy('publication_detail')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.publication = Publication.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)


class CommentListView(ListView):
    model = Comment
    template_name = 'publication/publication_detail.html'
    context_object_name = 'comments'

    def get_queryset(self):
        return Comment.objects.filter(publication__pk=self.kwargs['pk']).order_by('created_at')
