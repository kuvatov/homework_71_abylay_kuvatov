from rest_framework import viewsets

from api.serializers import PublicationSerializer
from instagram.models import Publication


class PublicationViewSet(viewsets.ModelViewSet):
    queryset = Publication.objects.filter(is_deleted=False)
    serializer_class = PublicationSerializer
