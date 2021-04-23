from django.db import models
from django.contrib.auth.models import User

from accounts.models import  Team

# Create your models here.


class Response(models.Model):
    team=models.ForeignKey(Team, null=True, on_delete=models.CASCADE)
    response = models.TextField()
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    

    def __str__(self):
        return (str(self.user.username) + " - response")


