from ast import literal_eval
import pandas as pd
from rest_framework.response import Response

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from rest_framework.views import APIView
from rest_framework import viewsets, permissions, status
movies_df = pd.read_csv("./users_movie.csv")
genres_df = pd.read_csv("./users_genre.csv")

movies_df = pd.merge(movies_df, genres_df, on='genre_id')

movies_columns = movies_df[['movie_id', 'genre', 'name', 'actors', 'director']]


def clean_data(row):
    if isinstance(row, list):
        return [str.lower(i.replace(" ", "")) for i in row]
    else:
        if isinstance(row, str):
            return str.lower(row.replace(" ", ""))
        else:
            return ""


features = ['actors', 'director', 'genre']
for feature in features:
    movies_columns[feature] = movies_columns[feature].apply(clean_data)


def create_soup(x):
    return ' '.join(x['actors']) + ' ' + x['director']


movies_columns["soup"] = movies_columns.apply(create_soup, axis=1)

print(movies_columns["soup"].head())
count_vectorizer = CountVectorizer(stop_words="english")
count_matrix = count_vectorizer.fit_transform(movies_columns["soup"])

cosine_sim2 = cosine_similarity(count_matrix, count_matrix)

movies_columns = movies_columns.reset_index()

indices = pd.Series(movies_columns.index,
                    index=movies_columns['name']).drop_duplicates()


def get_recommendations(name, cosine_sim=cosine_sim2):

    idx = indices[name]
    sim_scores = list(enumerate(cosine_sim[idx]))

    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:10]
    # (a, b) where a is id of movie, b is sim_score

    movies_indices = [ind[0] for ind in sim_scores]
    movies = movies_columns["name"].iloc[movies_indices]
    return movies


class ForYou(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        moviename = request.data['moviename']

        my_result = get_recommendations(moviename)
        print(my_result)
        return Response(my_result)
