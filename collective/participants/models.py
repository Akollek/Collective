from django.db import models

class Participant(models.Model):
    number   = models.CharField(max_length=20)
    username = models.CharField(max_length=200)
    joined   = models.DateTimeField('time joined')
    score    = models.IntegerField(default=0)
    played   = models.IntegerField(default=0)
