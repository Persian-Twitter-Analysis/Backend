from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    id = serializers.CharField()
    tweeter_id = serializers.CharField()
    images_sentiments = serializers.CharField()
    tweets_sentiments = serializers.CharField()
    friends_sentiments = serializers.CharField()
    images_distance = serializers.CharField()
    tweets_distance = serializers.CharField()
    images_tweets_distance = serializers.CharField()
    images_topics = serializers.CharField()
    tweets_topics = serializers.CharField()