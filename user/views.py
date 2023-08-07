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

class User(APIView):

    def get(self, request):
        print(request.GET.get('username', ''))
        username = request.GET.get('username', '')
        user = UserModel.objects.filter(tweeter_id=username)[0]
        serialized_obj = UserSerializer(user)
        obj = JSONRenderer().render(serialized_obj.data)
        return Response({"data": obj}, status=status.HTTP_200_OK)
    