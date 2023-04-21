from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from api.serializers import PublicationSerializer, LikeSerializer, CommentSerializer
from instagram.models import Publication, Like, Comment


class PublicationViewSet(viewsets.ModelViewSet):
    queryset = Publication.objects.filter(is_deleted=False)
    serializer_class = PublicationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        publication = serializer.instance
        if publication.user == self.request.user:
            serializer.save()
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

    def perform_destroy(self, instance):
        user = self.request.user
        if instance.user == user:
            instance.delete()
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_destroy(self, instance):
        user = self.request.user
        if instance.user == user:
            instance.delete()
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
