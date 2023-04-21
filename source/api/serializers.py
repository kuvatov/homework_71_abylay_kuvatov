from rest_framework import serializers

from instagram.models import Publication, Like


class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        exclude = ('is_deleted', 'deleted_at')


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('user', 'publication', 'created_at')
