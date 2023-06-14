from django.shortcuts import render
from rest_framework.response import Response 
from rest_framework.decorators import api_view 

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer 
from rest_framework_simplejwt.views import TokenObtainPairView


""" Iclude uername in token object using the Token obtain pair view"""
class MyTokenSerializer(TokenObtainPairSerializer):
    @classmethod 

    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        
        return token  

""" Token view """
class MyTokenView(TokenObtainPairView):
    serializer_class = MyTokenSerializer


# @api_view(['GET'])
# def getRoutes(request):
#     routes = [
#         '/api/token',
#         '/api/token/refresh',
#     ]

#     return Response(routes)