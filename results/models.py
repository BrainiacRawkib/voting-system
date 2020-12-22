from django.db import models
from django.contrib.auth.models import User
from django.db.models import Count, Sum
from django.utils.timezone import now
from states.models import LGA, PollingUnit
from party.models import Party


class AnnouncedLGAResult(models.Model):
    lga_name = models.ForeignKey(LGA, related_name='lga_results', on_delete=models.CASCADE)
    party_abbr = models.ForeignKey(Party, related_name='lga_party_score', on_delete=models.CASCADE)
    agent = models.ForeignKey(User, on_delete=models.CASCADE)
    party_score = models.PositiveIntegerField()
    date = models.DateTimeField(default=now)

    def __str__(self):
        return f'{self.lga_name}, {self.party_abbr} Score'
    


class AnnouncedPUResult(models.Model):
    pu_id = models.ForeignKey(PollingUnit, related_name='pu_results', on_delete=models.CASCADE)
    party_abbr = models.ForeignKey(Party, related_name='pu_party_score', on_delete=models.CASCADE)
    agent = models.ForeignKey(User, on_delete=models.CASCADE)
    party_score = models.PositiveIntegerField()
    date = models.DateTimeField(default=now)

    def total_result(self):
        results = AnnouncedPUResult.objects.aggregate(Sum('party_score'))
        return results

    def __str__(self):
        return f'{self.pu_id}, {self.party_abbr} Score'
    