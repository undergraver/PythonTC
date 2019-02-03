from rest_framework import serializers
from tcapp.models import Post, Like, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','email','password','first_name','last_name')

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id','userId','pubDate','text')

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('id','postId','userId')

