from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.views import View

from instagram.models import Like, Publication


class LikeCreateView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        publication_id = kwargs['pk']
        publication = Publication.objects.get(id=publication_id)
        try:
            like = Like.objects.get(publication=publication, user=request.user)
            like.delete()
            publication.likes_count -= 1
        except Like.DoesNotExist:
            like = Like.objects.create(publication=publication, user=request.user)
            publication.likes_count += 1
        publication.save()
        return JsonResponse({'likes_count': publication.likes_count})
