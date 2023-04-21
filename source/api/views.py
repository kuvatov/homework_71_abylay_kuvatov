from rest_framework import viewsets

from api.serializers import PublicationSerializer, LikeSerializer
from instagram.models import Publication, Like


class PublicationViewSet(viewsets.ModelViewSet):
    queryset = Publication.objects.filter(is_deleted=False)
    serializer_class = PublicationSerializer


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
