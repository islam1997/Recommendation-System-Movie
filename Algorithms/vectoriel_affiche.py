import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
import math
import nltk
import re
from stop_words import get_stop_words
import json



class VectorielModel:
    def __init__(self, path="data\\ml-small"):
        self.movies = pd.read_csv(path + "\\movies.csv")
        self.tags = pd.read_csv(path + "\\tags.csv")
        self.ratings = pd.read_csv(path + "\\ratings_train_s.csv")
        self.lod = pd.read_csv("more_data.csv")
        self.lod = self.lod[self.lod.subj.notna()]
        ff = open('more_data2.json')
        self.lod2 = json.load(ff)
        self.indexes = []
        self.movie_vectors = None
        self.profile_vector = None

    def create_item_vectors(self, view_vect=False, nb_vect=0, lodP=False):

        if lodP:
            filename = "dataAvecLOD.json"
        else:
            filename = "dataSansLOD.json"
        ff = open(filename)
        i_dict = json.load(ff)
        i_list = i_dict.values()
        tfidf_vectorizer = TfidfVectorizer(use_idf=True, stop_words="english")
        self.movie_vectors = tfidf_vectorizer.fit_transform(i_list)

        if view_vect:
            single_vect = self.movie_vectors[nb_vect]
            df = pd.DataFrame(single_vect.T.todense(), index=tfidf_vectorizer.get_feature_names(), columns=["tfidf"])
            df = df.sort_values(by=["tfidf"], ascending=False)
            with pd.option_context("display.max_rows", None):
                print(df)

    def create_user_profile(self, active_user):
        user_id = active_user
        active_user_ratings = self.ratings[self.ratings.userId == user_id]
        active_user_ratings['weight'] = active_user_ratings['rating'] / 5
        self.indexes.clear()
        for idd in np.array(active_user_ratings['movieId'].values):
            self.indexes.append(self.movies.index[self.movies['movieId'] == idd].values.item())

        self.profile_vector = np.dot(self.movie_vectors[np.array(self.indexes)].toarray().T,
                                     active_user_ratings['weight'].values)

    def get_recommandation(self, nb_recomm=10):
        sim_matrix = pd.DataFrame(cosine_similarity(np.atleast_2d(self.profile_vector), self.movie_vectors))
        recommandation_list = sim_matrix.transpose().sort_values(0, ascending=False)
        ccc = 0
        similarity = {}
        for i in list(recommandation_list[0].keys()):
            similarity[i] = list(recommandation_list[0].values)[ccc]
            ccc = ccc+1
        #with pd.option_context("display.max_rows", None):
         #   print(recommandation_list[:nb_recomm])
        recommandation_list = recommandation_list.transpose().columns.values

        #with pd.option_context("display.max_rows", None):
        #    print(self.movies['title'][recommandation_list][:nb_recomm])
        recommandation_list = [item for item in recommandation_list if item not in self.indexes]
        for k in list(similarity.keys()):
            if k not in recommandation_list:
                del similarity[k]
        return similarity

def affiche_list_vect(active_user_id, nn, lodp):
    recommender = VectorielModel(path="data\\ml-1m")
    recommender.create_item_vectors(lodP=lodp)
    recommender.create_user_profile(active_user=active_user_id)
    sim = recommender.get_recommandation(nb_recomm=nn)
    movies = recommender.movies
    for i in list(sim.keys())[:nn]:
        liss = list(movies[movies.movieId == i]['title'].values)
        if len(liss) != 0:
            sim[i] = liss[0]
    dat = ""
    for i in list(sim.keys())[:nn]:
        dat = dat + str(i) + "    " + str(sim[i]) + " \n"
    return dat




