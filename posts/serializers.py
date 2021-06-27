from rest_framework import serializers

from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'body', 'id']


class LikesSerializer(serializers.Serializer):
    post = serializers.UUIDField()


class LikesStatisitcsSerializer(serializers.Serializer):
    date_from = serializers.DateField()
    date_to = serializers.DateField()
