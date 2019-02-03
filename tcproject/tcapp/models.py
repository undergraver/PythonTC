from django.db import models
from django.contrib.auth.models import AbstractUser

import pyhunter
import clearbit

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

import os

def CheckIfEmailIsGood(value):
    information = None
    try:
        ph = pyhunter.PyHunter(os.getenv('HUNTER_API_KEY','bogus'))
        information = ph.email_verifier(value)
    except:
        # ignore in case some connectivity issue happens
        pass

    if information is not None:
        if information['result'] == 'undeliverable':
            raise ValidationError(
            _('Hunter says %s is an invalid email.') % (value)
            )

class User(AbstractUser):
    email = models.EmailField(unique=True,validators=[CheckIfEmailIsGood])
    def clean(self):
        super(User,self).clean()
        if not self.is_active:
            self.is_active = True
        # complete if first_name and last_name is empty
        if self.first_name == "" and self.last_name == "":
            clearbit.key = os.getenv('CLEARBIT_KEY','bogus')
            try:
                response = clearbit.Enrichment.find(email=self.email, stream=True)
                print(response)
                if 'person' in response:
                    self.first_name = response['person']['name']['givenName']
                    self.last_name = response['person']['name']['familyName']
            except:
                pass
                # test
                #self.first_name = "no clearbit api key - signup failed"
                #self.last_name = "no nice last name, sorry"
 
    def save(self, **kwargs):
        self.clean()
        return super(User, self).save(**kwargs)

class Post(models.Model):
    userId = models.ForeignKey(User,on_delete=models.CASCADE)
    pubDate = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

class Like(models.Model):
    postId = models.ForeignKey(Post,on_delete=models.CASCADE)
    userId = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        unique_together = ('postId', 'userId',)
