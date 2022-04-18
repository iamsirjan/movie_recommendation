from dataclasses import fields
from os import read
from unittest.util import _MAX_LENGTH
from django.forms import models
from django.http import request
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from users.models import genre, language, movie, rating

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    firstname = serializers.CharField(
        required=True,

    )
    lastname = serializers.CharField(
        required=True,

    )
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    re_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('user_id', 'username', 'email', 'firstname',
                  'lastname', 'password', 're_password', 'is_active', 'is_admin')
        extra_kwargs = {'user_id': {'read_only': True}, 'password': {'write_only': True}, 're_password': {'write_only': True},
                        'username': {'write_only': True}, 'lastname': {'read_only': True}, 'is_active': {'read_only': True}, 'is_admin': {'read_only': True}}

    def validate(self, attrs):
        if attrs['password'] != attrs['re_password']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'], password=validated_data['password'], username=validated_data['username'], firstname=validated_data['firstname'], lastname=validated_data['lastname'])
        return user


class LanguageSerializer(serializers.HyperlinkedModelSerializer):
    language = serializers.CharField(required=True,)

    class Meta:
        model = language
        fields = (
            'language', 'language_id'
        )


class GenreSerializer(serializers.HyperlinkedModelSerializer):
    genre = serializers.CharField(required=True)

    class Meta:
        model = genre
        fields = (
            'genre', 'genre_id'
        )


class MovieSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True,)
    video = serializers.CharField(required=True,)

    genre = serializers.PrimaryKeyRelatedField(
        queryset=genre.objects.all(), many=True)

    language = serializers.PrimaryKeyRelatedField(
        queryset=language.objects.all(), many=True)

    class Meta:
        model = movie
        fields = (
            'movie_id',
            'name',
            'video',
            'language',
            'genre',

        )


class RatingSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = rating
        fields = (
            'rating_id',
            'rating',
            'comment',
            'user',
            'movie',
        )