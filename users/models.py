from statistics import mode
from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
# Create your models here.


class user(AbstractUser, PermissionsMixin):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=20)
    email = models.EmailField(unique=True)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.email


class genre(models.Model):
    genre_id = models.AutoField(primary_key=True)

    genre = models.CharField(max_length=20)

    def __str__(self):
        return self.genre


class language(models.Model):
    language_id = models.AutoField(primary_key=True)

    language = models.CharField(max_length=20)

    def __str__(self):
        return self.language


class movie(models.Model):
    movie_id = models.AutoField(primary_key=True)

    name = models.CharField(unique=True, max_length=100)
    video = models.CharField(max_length=1000)
    # images = models.ImageField('images')

    language = models.ForeignKey(language, on_delete=models.CASCADE, null=True, blank=True
                                 )
    genre = models.ForeignKey(genre, on_delete=models.CASCADE, null=True, blank=True, related_name='movies'
                              )


class rating(models.Model):
    rating_id = models.AutoField(primary_key=True)

    rating = models.IntegerField()
    comment = models.CharField(max_length=200)
    user = models.ForeignKey(user, on_delete=models.CASCADE,
                             )
    movie = models.ForeignKey(movie, on_delete=models.CASCADE,
                              )
