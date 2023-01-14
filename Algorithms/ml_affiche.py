import numpy as np
import pandas as pd
import math
import nltk
from nltk.corpus import stopwords
from stop_words import get_stop_words
import re
import json





def affiche_list_ml(active_user, nn, lodp):
    nltk_words = list(stopwords.words("english"))
    stop_words = list(get_stop_words("en"))
    stop_words.extend(nltk_words)
    stemmer = nltk.stem.PorterStemmer()

    movies = pd.read_csv("data\\ml-1m\\movies.csv")
    tags = pd.read_csv("data\\ml-1m\\tags.csv")
    ratings = pd.read_csv("data\\ml-1m\\ratings_train_s.csv")

    ff = open('more_data2.json')
    lod2 = json.load(ff)

    lod = pd.read_csv("more_data.csv")
    lod = lod[lod.subj.notna()]

    if lodp:
        filename = "dataAvecLOD2.json"
    else:
        filename = "dataSansLOD2.json"
    ff = open(filename)
    i_dict = json.load(ff)

    active_user_id = active_user
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
    j_dict = {}
    comp = {}

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

    sim = my_dict
    for i in list(sim.keys())[:nn]:
        liss = list(movies[movies.movieId == int(i)]['title'].values)
        if len(liss) != 0:
            sim[i] = liss[0]
    dat = ""
    for i in list(sim.keys())[:nn]:
        dat = dat + str(i) + "    " + str(sim[i]) + " \n"

    return dat
