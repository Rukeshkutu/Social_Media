from post.models import Post, PostAttachment
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = {'id', 'body', 'created_by','created_at'}
