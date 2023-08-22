from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
from .models import User as UserModel
from .serializer import UserSerializer
from rest_framework.renderers import JSONRenderer
from django.db.models.functions import Length

from dist import distance

class User(APIView):

    def get(self, request):
        print(request.GET.get('username', ''))
        username = request.GET.get('username', '')
        user = UserModel.objects.filter(tweeter_id=username)
        if len(user) == 0:
            return Response({"data": "USER_NOT_FOUND"}, status=status.HTTP_200_OK)
       
        serialized_obj = UserSerializer(user[0])
        obj = JSONRenderer().render(serialized_obj.data)
        return Response({"id": user[0].id, "tweeter_id": user[0].tweeter_id, "images_sentiments": user[0].images_sentiments, "tweets_sentiments": user[0].tweets_sentiments, "friends_sentiments": user[0].friends_sentiments, "images_distance": user[0].images_distance, "tweets_distance": user[0].tweets_distance, "images_tweets_distance": user[0].images_tweets_distance, "images_topics": user[0].images_topics, "tweets_topics": user[0].tweets_topics}, status=status.HTTP_200_OK, content_type="application/json")
    