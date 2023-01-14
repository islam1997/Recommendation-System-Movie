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
        self.lod = pd.read_csv("data\\more_data.csv")
        self.lod = self.lod[self.lod.subj.notna()]
        ff = open('data\\more_data2.json')
        self.lod2 = json.load(ff)
        self.indexes = []
        self.movie_vectors = None
        self.profile_vector = None

    def create_item_vectors(self, view_vect=False, nb_vect=0, lodP=False):

        i_dict = {}
        nltk_words = list(stopwords.words("english"))
        stop_words = list(get_stop_words("en"))
        stop_words.extend(nltk_words)
        stemmer = nltk.stem.PorterStemmer()

        for m_id, title, genre in self.movies.values:
            temp = str(genre).lower().replace('|', ' ')
            temp = temp + " " + str(title).lower()
            temp = re.sub(r'[^\w\s]', '', temp)
            i_dict[m_id] = ''
            """
            if m_id in lod['movieId'].values:
                pp = str(lod[lod.movieId == m_id]['subj'].values[0]).replace("http://dbpedia.org/resource/Category:",
                                                                             "")
                pp = pp.replace('_', ' ')
                temp = temp + pp.replace("\'", "")
            if str(m_id) in lod2.keys():
                temp = temp + lod2[str(m_id)].replace("'", '')
                """
            for u_id, id2, tag, time in self.tags.values:
                if m_id == id2:
                    temp = temp + " " + str(tag).lower()
                    temp = re.sub(r'[^\w\s]', '', temp)

            for tt in nltk.word_tokenize(temp):
                if tt not in stop_words:
                    i_dict[m_id] = i_dict[m_id] + " " + tt

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

        print(self.indexes)
        self.profile_vector = np.dot(self.movie_vectors[np.array(self.indexes)].toarray().T,
                                     active_user_ratings['weight'].values)
        print(self.movie_vectors[np.array(self.indexes)].toarray().T)
        print(self.profile_vector)

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



def affiche_tests_vect(nbusers, lodp):
    idcg = {10: 4.5432,
            15: 5.8608,
            20: 7.0395,
            30: 9.1567}
    recommender = VectorielModel(path="data\\ml-1m")
    recommender.create_item_vectors(lodP=lodp)

    test = pd.read_csv('data\\ml-1m\\ratings_test_s.csv')

    active_user_id = 889
    testlist = list(test[test.userId == active_user_id]['movieId'])
    ids = list(test.userId.unique())[:nbusers]
    results = []
    for nn in [10, 15, 20, 30]:
        tp = 0
        tn = 0
        for idd in ids:
            active_user_id = idd
            recommender.create_user_profile(active_user=active_user_id)
            sim = recommender.get_recommandation(nb_recomm=nn)
            recommandations = list(sim.keys())[:nn]
            nb = 0
            cnt = 0
            ndcg = 0
            for i in recommandations:
                cnt = cnt + 1
                for j in testlist:
                    if i == j:
                        nb = nb + 1
                        ndcg = ndcg + (1 / math.log2(cnt + 1))
            ndcg = ndcg / idcg[nn]
            tp = tp + ((nb / nn) * len(test[test.userId == active_user_id]))
            tn = tn + (ndcg * len(test[test.userId == active_user_id]))
            print(tp, ' ', active_user_id)
        results.append((tp / (len(test[test['userId'].isin(ids)])), tn / (len(test[test['userId'].isin(ids)]))))
    return results



""";
movies = pd.read_csv("data\\ml-small\\movies.csv")
tags = pd.read_csv("data\\ml-small\\tags.csv")
ratings = pd.read_csv("data\\ml-small\\ratings.csv")

i_dict = {}
for m_id, title, genre in movies.values:
    i_dict[m_id] = str(genre).lower().replace('|', ' ')
    for u_id, id2, tag, time in tags.values:
        if m_id == id2:
            i_dict[m_id] = i_dict[m_id] + " " + str(tag).lower()

i_list = i_dict.values()
print(i_dict[1834])


tfidf_vectorizer = TfidfVectorizer(use_idf=True, stop_words="english")
movie_vectors = tfidf_vectorizer.fit_transform(i_list)


single_vect = movie_vectors[0]
df = pd.DataFrame(single_vect.T.todense(), index=tfidf_vectorizer.get_feature_names(), columns=["tfidf"])
df = df.sort_values(by=["tfidf"], ascending=False)
with pd.option_context("display.max_rows", None):
    print(df)


active_user_id = 1
active_user_ratings = ratings[ratings.userId == active_user_id]
active_user_ratings['weight'] = active_user_ratings['rating']/5

indexes = []
for idd in np.array(active_user_ratings['movieId'].values):
    indexes.append(movies.index[movies['movieId'] == idd].values.item())

profile_vector = np.dot(movie_vectors[np.array(indexes)].toarray().T,
                        active_user_ratings['weight'].values)

sim_matrix = pd.DataFrame(cosine_similarity(np.atleast_2d(profile_vector), movie_vectors))
recommandations = sim_matrix.transpose().sort_values(0, ascending=False)
print(recommandations)
recommandations = recommandations.transpose().columns.values
recommandations = [item for item in recommandations if item not in indexes][:10]

print(movies['title'][recommandations])
"""
