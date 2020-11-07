from rest_framework import serializers

from apps.blog.models import Post
from apps.users.models import User


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'content', 
            'published_on',
            'user',
        )
