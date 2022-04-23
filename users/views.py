import json
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, permissions, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from datetime import datetime
from users.models import genre, language, movie, rating

from .serializers import GenreSerializer, LanguageSerializer, MovieSerializer, RatingSerializer, UserSerializer
from rest_framework import generics


User = get_user_model()
MESSAGE = "Something went wrong."


class RegisterView(generics.CreateAPIView, generics.ListCreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer


class RetrieveUserView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        try:
            user = request.user
            user = UserSerializer(user)
            return Response({'user': user.data}, status=status.HTTP_200_OK)
        except Exception:
            return Response({'error': MESSAGE}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class GenreViewSet(generics.ListAPIView, generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = genre.objects.all()
    serializer_class = GenreSerializer


class LanguageViewSet(generics.ListAPIView, generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = language.objects.all()
    serializer_class = LanguageSerializer


class MovieViewSet(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = (permissions.IsAuthenticated,)

    queryset = movie.objects.all()
    serializer_class = MovieSerializer


class MovieGetViewSet(generics.ListAPIView):

    permission_classes = (permissions.AllowAny,)

    queryset = movie.objects.all()
    serializer_class = MovieSerializer


class RatingViewSet(generics.ListAPIView, generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)

    queryset = rating.objects.all()
    serializer_class = RatingSerializer
