from django.db import models
from django.contrib.auth.models import User


class Agent(models.Model):
    user = models.OneToOneField(User, related_name='agent', on_delete=models.CASCADE)
    phone = models.CharField(max_length=13)    

    def __str__(self):
        return f'{self.firstname, self.lastname}'
    
