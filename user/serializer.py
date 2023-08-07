from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=200)
    tweeter_id = serializers.CharField(max_length=200)
    images_sentiments = serializers.CharField(max_length=200)
    tweets_sentiments = serializers.CharField(max_length=200)
    friends_sentiments = serializers.CharField(max_length=200)
    images_distance = serializers.CharField(max_length=200)
    tweets_distance = serializers.CharField(max_length=200)
    images_topics = serializers.CharField(max_length=200)
    tweets_topics = serializers.CharField(max_length=200)