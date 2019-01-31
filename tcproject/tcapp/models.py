from django.db import models

# Create your models here.

class User(models.Model):
    email = models.EmailField()
    fullName = models.TextField()

class Post(models.Model):
    userId = models.ForeignKey(User,on_delete=models.CASCADE)
    pubDate = models.DateField(auto_now_add=True)

class Like(models.Model):
    postId = models.ForeignKey(Post,on_delete=models.CASCADE)
    userId = models.ForeignKey(User,on_delete=models.CASCADE)
