from django.urls import path
from .views import GenreViewSet, RegisterView, RetrieveUserView, MovieViewSet, LanguageViewSet, RatingViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path('register', RegisterView.as_view(), name="register_user"),
    path('me', RetrieveUserView.as_view(), name="retrieve_user"),
    path('token', TokenObtainPairView.as_view(), name='token'),
    path('movies/',
         MovieViewSet.as_view(), name='movies'),
    path('genre/',
         GenreViewSet.as_view(), name='genre'),

    path('language/',
         LanguageViewSet.as_view(), name='language'),

    path('rating/',
         RatingViewSet.as_view(), name='rating'),

]
