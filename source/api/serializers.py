from rest_framework import serializers

from instagram.models import Publication


class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        exclude = ('is_deleted', 'deleted_at')
