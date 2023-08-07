from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    tweeter_id = models.CharField(max_length=200)
    images_sentiments = models.CharField(max_length=200, default="", blank=True)
    tweets_sentiments = models.CharField(max_length=200, default="", blank=True)
    friends_sentiments = models.CharField(max_length=200, default="", blank=True)
    images_distance = models.CharField(max_length=200, default="", blank=True)
    tweets_distance = models.CharField(max_length=200, default="", blank=True)
    images_topics = models.CharField(max_length=200, default="", blank=True)
    tweets_topics = models.CharField(max_length=200, default="", blank=True)
