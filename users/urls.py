from django.urls import path

from users.containrecommender import ForYou
from .views import GenreViewSet, RegisterView, MovieApiAction, RetrieveUserView, MovieViewSet, LanguageViewSet, RatingViewSet, MovieGetViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from .recommender import MyView
urlpatterns = [
    path('register', RegisterView.as_view(), name="register_user"),
    path('movie/<movie_id>/', MovieApiAction.as_view()),
    path('me', RetrieveUserView.as_view(), name="retrieve_user"),
    path('token', TokenObtainPairView.as_view(), name='token'),
    path('movies/',
         MovieViewSet.as_view(), name='movies'),
    path('get-movies/',
         MovieGetViewSet.as_view(), name='movies'),
    path('genre/',
         GenreViewSet.as_view(), name='genre'),

    path('language/',
         LanguageViewSet.as_view(), name='language'),

    path('rating/',
         RatingViewSet.as_view(), name='rating'),


    path('recommender/',
         MyView.as_view(), name='recommend'),
    path('recommendedForYou/', ForYou.as_view(), name="foryou")
]
