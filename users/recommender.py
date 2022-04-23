from django.shortcuts import render
from rest_framework.response import Response
import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors
import matplotlib.pyplot as plt
import seaborn as sns
from rest_framework.views import APIView
from rest_framework import viewsets, permissions, status

from sklearn.metrics.pairwise import cosine_similarity
Movies = pd.read_csv("./movie.csv")
Ratings = pd.read_csv("./rating.csv")


Mean = Ratings.groupby(by="user_id", as_index=False)['rating'].mean()
print(Mean)
Rating_avg = pd.merge(Ratings, Mean, on='user_id')
Rating_avg['adg_rating'] = Rating_avg['rating_x']-Rating_avg['rating_y']
Rating_avg.head()
check = pd.pivot_table(Rating_avg, values='rating_x',
                       index='user_id', columns='movie_id')
check.head()
final = pd.pivot_table(Rating_avg, values='adg_rating',
                       index='user_id', columns='movie_id')
final.head()
# Replacing NaN by Movie Average
final_movie = final.fillna(final.mean(axis=0))

# Replacing NaN by user Average
final_user = final.apply(lambda row: row.fillna(row.mean()), axis=1)
print(final_movie.head())
print(final_user.head())

b = cosine_similarity(final_user)

np.fill_diagonal(b, 0)
similarity_with_user = pd.DataFrame(b, index=final_user.index)
print(similarity_with_user)
similarity_with_user.columns = final_user.index
similarity_with_user.head()

cosine = cosine_similarity(final_movie)
np.fill_diagonal(cosine, 0)
similarity_with_movie = pd.DataFrame(cosine, index=final_movie.index)
similarity_with_movie.columns = final_user.index
similarity_with_movie.head()


def find_n_neighbours(df, n):
    order = np.argsort(df.values, axis=1)[:, :n]
    df = df.apply(lambda x: pd.Series(x.sort_values(ascending=False)
                                      .iloc[:n].index, index=['top{}'.format(i) for i in range(1, n+1)]), axis=1)

    return df


sim_user_30_u = find_n_neighbours(similarity_with_user, 3)
print(sim_user_30_u.head())
sim_user_30_u.head()

sim_user_30_m = find_n_neighbours(similarity_with_movie, 3)
sim_user_30_m.head()


def get_user_similar_movies(user1, user2):
    common_movies = Rating_avg[Rating_avg.user_id == user1].merge(
        Rating_avg[Rating_avg.user_id == user2],
        on="movie_id",
        how="inner")
    return common_movies.merge(Movies, on='movie_id')


def User_item_score(user, item):
    a = sim_user_30_m[sim_user_30_m.index == user].values
    b = a.squeeze().tolist()
    c = final_movie.loc[:, item]
    d = c[c.index.isin(b)]
    f = d[d.notnull()]
    avg_user = Mean.loc[Mean['user_id'] == user, 'rating'].values[0]
    index = f.index.values.squeeze().tolist()
    corr = similarity_with_movie.loc[user, index]
    fin = pd.concat([f, corr], axis=1)
    fin.columns = ['adg_score', 'correlation']
    fin['score'] = fin.apply(lambda x: x['adg_score']
                             * x['correlation'], axis=1)
    nume = fin['score'].sum()
    deno = fin['correlation'].sum()
    final_score = avg_user + (nume/deno)
    return final_score


Rating_avg = Rating_avg.astype({"movie_id": str})
Movie_user = Rating_avg.groupby(
    by='user_id')['movie_id'].apply(lambda x: ','.join(x))


def User_item_score1(user):
    Movie_seen_by_user = check.columns[check[check.index == user].notna(
    ).any()].tolist()
    a = sim_user_30_m[sim_user_30_m.index == user].values
    b = a.squeeze().tolist()
    d = Movie_user[Movie_user.index.isin(b)]
    l = ','.join(d.values)
    Movie_seen_by_similar_users = l.split(',')
    Movies_under_consideration = list(
        set(Movie_seen_by_similar_users)-set(list(map(str, Movie_seen_by_user))))
    Movies_under_consideration = list(map(int, Movies_under_consideration))
    score = []
    for item in Movies_under_consideration:
        c = final_movie.loc[:, item]
        d = c[c.index.isin(b)]
        f = d[d.notnull()]
        avg_user = Mean.loc[Mean['user_id'] == user, 'rating'].values[0]
        index = f.index.values.squeeze().tolist()
        corr = similarity_with_movie.loc[user, index]
        fin = pd.concat([f, corr], axis=1)
        fin.columns = ['adg_score', 'correlation']
        fin['score'] = fin.apply(
            lambda x: x['adg_score'] * x['correlation'], axis=1)
        nume = fin['score'].sum()
        deno = fin['correlation'].sum()
        final_score = avg_user + (nume/deno)
        score.append(final_score)
    data = pd.DataFrame(
        {'movie_id': Movies_under_consideration, 'score': score})
    top_5_recommendation = data.sort_values(
        by='score', ascending=False).head(5)
    Movie_Name = top_5_recommendation.merge(Movies, how='inner', on='movie_id')
    Movie_Names = Movie_Name.movie_id.values.tolist()
    return Movie_Names


# user = 2
# predicted_movies = User_item_score1(user)

# # for i in predicted_movies:
# #     print(i)


class MyView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        userid = request.data['userid']

        my_result = User_item_score1(userid)
        print(my_result)
        return Response(my_result)
