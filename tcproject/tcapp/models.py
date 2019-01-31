from django.db import models

# Create your models here.

class TCUser(models.Model):
    email = models.EmailField()
    fullName = models.TextField()

class TCPost(models.Model):
    userId = models.ForeignKey(TCUser,on_delete=models.CASCADE)
    pubDate = models.DateField(auto_now_add=True)

class TCLike(models.Model):
    postId = models.ForeignKey(TCPost,on_delete=models.CASCADE)
    userId = models.ForeignKey(TCUser,on_delete=models.CASCADE)
