from django.test import TestCase
from .models import genre, movie, language, rating, user


class MovieTestCase(TestCase):

    def test_create_movie(self):
        movie.objects.create(
            name="the batman", video="https://www.youtube.com/watch?v=JLV26lOElSY&ab_channel=OSRDigital", actors='dayahang rai', director='ram babu gurung',)

    def test_language_create(self):
        language.objects.create(
            language="telgu"
        )

    def test_create_user(self):
        user.objects.create(
            username="nigam", firstname="nigam", lastname="kc", email="nigam@gmail.com", is_admin=1
        )

    def test_genre_create(self):
        genresname = genre.objects.create(
            genre="thriller"
        )

    def test_rating_create(self):
        rating.objects.create(
            rating=5, comment="nice movie",
            user=user.objects.create(
                username="nigam", firstname="nigam", lastname="kc", email="nigam@gmail.com", is_admin=1
            ),
            movie=movie.objects.create(
                name="the batman", video="https://www.youtube.com/watch?v=JLV26lOElSY&ab_channel=OSRDigital", actors='dayahang rai', director='ram babu gurung',)
        )


class LogInTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'nigam',
            'password': 'nigam'}
        user.objects.create_user(**self.credentials)

    def test_login(self):
        # send login data
        response = self.client.post(
            'http://127.0.0.1:8000/users/token', self.credentials, follow=True)
        # should be logged in now
