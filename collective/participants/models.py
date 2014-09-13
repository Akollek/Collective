from django.db import models

class Participant(models.Model):
    number   = models.CharField(max_length=20)
    username = models.CharField(max_length=200)
    score    = models.IntegerField(default=0)
    played   = models.IntegerField(default=0)

class Cart(models.Model):
    x = models.CharField(max_length=1)
    y = models.CharField(max_length=1)
    o = models.CharField(max_length=1)

