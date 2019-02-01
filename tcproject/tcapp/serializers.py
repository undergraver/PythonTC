from rest_framework import serializers
from tcapp.models import User, Post, Like

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField(required=True)
    fullName = serializers.TextField(required=False,allow_blank=True)

    def create(self,validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.fullName = validated_data.get('fullName', instance.fullName)
        return instance

class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    userId = serializers.IntegerField(required=True)
    pubDate = serializers.DateField()

    def create(self,validated_data):
        return Post.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.userId = validated_data.get('userId',instance.userId)
        instance.pubDate = validated_data.get('pubDate',instance.pubDate)

class Like(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    postId = serializers.IntegerField(required=True)
    userId = serializers.IntegerField(required=True)

    def create(self,validated_data):
        return Like.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.postId = validated_data.get('postId',instance.postId)
        instance.userId = validated_data.get('userId',instance.userId)