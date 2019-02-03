from django.db import models

class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200,blank=True)
    last_name = models.CharField(max_length=200,blank=True)

    def __str__(self):
        return self.email

class Post(models.Model):
    userId = models.ForeignKey(User,on_delete=models.CASCADE)
    pubDate = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

class Like(models.Model):
    postId = models.ForeignKey(Post,on_delete=models.CASCADE)
    userId = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        unique_together = ('postId', 'userId',)
