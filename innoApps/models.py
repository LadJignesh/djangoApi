from django.db import models

class Challenge(models.Model):
  name =  models.CharField(max_length=50)
  about= models.CharField(max_length=200)

  def __str__(self):
    return self.name

class ChallengeData(models.Model):
  name =  models.CharField(max_length=50)
  instruction = models.CharField(max_length=300)
  mix= models.IntegerField()
  match = models.IntegerField()

  def __str__(self):
    return self.name

class SubmitChallenge(models.Model):
  mix= models.CharField(max_length=30)
  match= models.CharField(max_length=30)
  name= models.CharField(max_length=30)
  idea= models.CharField(max_length=100)
  code= models.CharField(max_length=5)

  def __str__(self):
    return self.name

