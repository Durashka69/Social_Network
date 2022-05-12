from rest_framework import serializers, exceptions
from .models import User, Post, Like


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('id', 'user', 'post')

    def validate(self, attrs):
        if Like.objects.filter(user=attrs['user'], post=attrs['post']).first():
            raise exceptions.ValidationError({'Error': 'Like already exists'})
        else:
            return attrs

class PostSerializer(serializers.ModelSerializer):
    likes = LikeSerializer(read_only=True, many=True)
    
    class Meta:
        model = Post
        fields = ('id', 'title', 'author', 'content',
                  'date_created', 'date_updated', 'likes')
