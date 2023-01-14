import numpy as np
import pandas as pd
import math
import nltk
from nltk.corpus import stopwords
from stop_words import get_stop_words
import re
import json




def affiche_tests_ml(nbusers, lodp):
    ff = open('data\\more_data2.json')
    lod2 = json.load(ff)

    movies = pd.read_csv("data\\ml-1m\\movies.csv")
    tags = pd.read_csv("data\\ml-1m\\tags.csv")
    ratings = pd.read_csv("data\\ml-1m\\ratings_train_s.csv")

    lod = pd.read_csv("data\\more_data.csv")
    lod = lod[lod.subj.notna()]

    i_dict = {}
    nltk_words = list(stopwords.words("english"))
    stop_words = list(get_stop_words("en"))
    stop_words.extend(nltk_words)
    stemmer = nltk.stem.PorterStemmer()

    for m_id, title, genre in movies.values:
        if lodp:
            filename = "data\\dataAvecLOD2.json"
        else:
            filename = "data\\dataSansLOD2.json"
        ff = open(filename)
        i_dict = json.load(ff)

    test = pd.read_csv('data\\ml-1m\\ratings_test_s.csv')
    ids = list(test.userId.unique())[:nbusers]
    results = []
    tp = 0
    tn = 0
    hh = 0
    for nn in [10, 15, 20, 30]:
        for idd in ids:
            active_user_id = idd
            user_profile = {}
            cnt = []
            user = {}

            for u_id, m_id, r, t in ratings.values:
                if u_id == active_user_id:
                    word_list = set(nltk.word_tokenize(i_dict[str(m_id)]))
                    user[m_id] = r/5
                    for word in word_list:
                        if word not in stop_words:
                            if user_profile.__contains__(word):
                                user_profile[word] = user_profile[word] + r/5
                            else:
                                user_profile[word] = r/5
                            cnt.append(word)

            for word in user_profile.keys():
                user_profile[word] = user_profile[word] / cnt.count(word)

            collection = []
            for words in i_dict.values():
                collection.extend(words.split(" "))

            word_count_c = {}

            for word in set(collection):
                word_count_c[word] = collection.count(word)

            cl = len(collection)
            µ = 0.75
            """
        word_dict_u = {}
        teta = 0.75
        du = len(user_profile)
        for word in set(user_profile):
            tf_u = user_profile.count(word)
            tf_c = word_count_c[word]
            word_dict_u[word] = ((teta * (tf_u / du)) + ((1 - teta) * (tf_c / cl)))
            """
            j_dict = {}
            """
        for m_id, words in i_dict.items():
            dl = len(words.split(" "))
            teta = 0.75
            p_q_md = 1
            word_dict_d = {}
            for word in set(user_profile):
                tf_d = str(words).count(word+" ")
                tf_c = word_count_c[word]
                word_dict_d[word] = ((teta * (tf_d/dl)) + ((1-teta) * (tf_c/cl)))
            j_dict[m_id] = word_dict_d
            """
            comp = {}

            #for m_id, words in i_dict.items():
                #print(m_id, ' ', words)

            for m_id, words in i_dict.items():
                words = words.split(" ")
                dl = len(words)
                teta = 0.75
                p_q_md = 0
                movie_count = 0
                for movie in user.keys():
                    for word in set(i_dict[str(movie)].split(" ")):
                        tf_d = words.count(word)
                        tf_c = word_count_c[word]
                        #if m_id == 296:
                        #print(movie, " ", tf_d, " ", dl, " ", math.log10(user[movie] * ((teta * (tf_d/dl)) + ((1-teta) * (tf_c/cl)))))
                        p_q_md = p_q_md + math.log10(user[movie] * ((teta * (tf_d/dl)) + ((1-teta) * (tf_c/cl))))
                comp[m_id] = p_q_md / len(user.keys())

            dl = len(cnt)
            calib = 0
            for word in set(user_profile.keys()):
                tf_d = cnt.count(word)
                tf_c = word_count_c[word]
                calib = calib + math.log10(user_profile[word] * ((teta * (tf_d / dl)) + ((1 - teta) * (tf_c / cl))))


            my_dict = dict(sorted(comp.items(), key=lambda item: item[1], reverse=True))

            for k in my_dict.keys():
                my_dict[k] = - my_dict[k]
                #my_dict[k] = 1 - math.log2(1 + (1 * ((my_dict[k] - 0) / -calib)))
            for k in user.keys():
                if k in list(my_dict.keys()):
                    del my_dict[k]

            testlist = list(test[test.userId == active_user_id]['movieId'])
            print(testlist)
            recommandations = list(my_dict.keys())[:nn]
            idcg = {10: 4.5432,
                    15: 5.8608,
                    20: 7.0395,
                    30: 9.1567}
            nb = 0
            cnt = 0
            ndcg = 0
            for i in recommandations:
                cnt = cnt + 1
                for j in testlist:
                    if str(i) == str(j):
                        nb = nb + 1
                        ndcg = ndcg + (1 / math.log2(cnt + 1))
            ndcg = ndcg / idcg[nn]

            tp = tp + ((nb/nn) * len(test[test.userId == active_user_id]))
            tn = tn + (ndcg * len(test[test.userId == active_user_id]))
            print(tp, ' ', active_user_id)
        results.append((tp/(len(test[test['userId'].isin(ids)])), tn/(len(test[test['userId'].isin(ids)]))))

    return results
