from django.db import models


class Party(models.Model):
    name = models.CharField(max_length=11)

    def __str__(self):
        return f'{self.name}'
    
