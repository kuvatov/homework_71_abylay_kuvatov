from rest_framework import serializers

from instagram.models import Publication


class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = ('user', 'image', 'description', 'likes_count', 'comments_count', 'created_at', 'edited_at')
