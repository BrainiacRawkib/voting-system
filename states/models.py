from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from . import choices

class State(models.Model):
    name = models.CharField(max_length=50, choices=choices.states, default='Abia')

    def __str__(self):
        return f'{self.name}'


class LGA(models.Model):
    name = models.CharField(max_length=50)
    state = models.ForeignKey(State, related_name='states', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("results:summed-results", kwargs={"name": self.name})
    

    def __str__(self):
        return f'{self.name}'
    

class Ward(models.Model):
    name = models.CharField(max_length=50)
    lga = models.ForeignKey(LGA, related_name='lgas', on_delete=models.CASCADE)
    state = models.ForeignKey(State, related_name='ward_states', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'


class PollingUnit(models.Model):
    name = models.CharField(max_length=50)
    lga = models.ForeignKey(LGA, related_name='pu_lgas', on_delete=models.CASCADE)
    state = models.ForeignKey(State, related_name='pu_states', on_delete=models.CASCADE)
    agent = models.ForeignKey(User, related_name='agents', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'