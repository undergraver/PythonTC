from rest_framework import serializers
from tcapp.models import User, Post, Like

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','email','fullName')

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id','userId','pubDate','text')

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('id','postId','userId')

