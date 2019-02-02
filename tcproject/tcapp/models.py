from django.db import models

from django.conf import settings

class Post(models.Model):
    userId = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    pubDate = models.DateField(auto_now_add=True)
    text = models.TextField()

class Like(models.Model):
    postId = models.ForeignKey(Post,on_delete=models.CASCADE)
    userId = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    class Meta:
        unique_together = ('postId', 'userId',)
