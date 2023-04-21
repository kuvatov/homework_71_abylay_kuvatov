from rest_framework import serializers

from instagram.models import Publication, Like


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('user', 'publication', 'created_at')


class PublicationSerializer(serializers.ModelSerializer):
    likes = LikeSerializer(many=True, read_only=True)

    class Meta:
        model = Publication
        exclude = ('is_deleted', 'deleted_at')
