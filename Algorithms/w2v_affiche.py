import numpy as np
import pandas as pd
from nltk.corpus import stopwords
from stop_words import get_stop_words
import nltk
import re
import json
from scipy import spatial
import math

import json


def affiche_list_w2v(active_user, nn, lodp):
    from gensim.models import Word2Vec, KeyedVectors, FastText
    ff = open('more_data2.json')
    lod2 = json.load(ff)

    movies = pd.read_csv("data\\ml-1m\\movies.csv")
    tags = pd.read_csv("data\\ml-1m\\tags.csv")
    ratings = pd.read_csv("data\\ml-1m\\ratings_train_s.csv")

    lod = pd.read_csv("more_data.csv")
    lod = lod[lod.subj.notna()]

    nltk_words = list(stopwords.words("english"))
    stop_words = list(get_stop_words("en"))
    stop_words.extend(nltk_words)
    i_dict = {}

    for m_id, title, genre in movies.values:
        temp = str(genre).lower().replace('|', ' ')
        temp = temp + " " + str(title).lower()
        temp = re.sub(r'[^\w\s]', '', temp)
        i_dict[m_id] = ''

        if lodp:
            if m_id in lod['movieId'].values:
                pp = str(lod[lod.movieId == m_id]['subj'].values[0]).replace("http://dbpedia.org/resource/Category:", "")
                pp = pp.replace('_', ' ')
                temp = temp + pp.replace("\'", "")
            if str(m_id) in lod2.keys():
                temp = temp + lod2[str(m_id)]
        else:
            for u_id, id2, tag, time in tags.values:
                if m_id == id2:
                    temp = temp + " " + str(tag).lower()
                    temp = re.sub(r'[^\w\s]', '', temp)
        for tt in nltk.word_tokenize(temp):
            if tt not in stop_words:
                i_dict[m_id] = i_dict[m_id] + " " + tt

    """
    trainVec = [nltk.word_tokenize(desc.lower()) for desc in desclist]
    model = Word2Vec(min_count = 1, vector_size=200, window=3, sample=6e-5, alpha=0.03, negative=10)
    model.build_vocab(trainVec)

    model.train(trainVec, total_examples=model.corpus_count, epochs=10)
    """
    model = KeyedVectors.load_word2vec_format('data\\GoogleNews-vectors-negative300.bin',
                                          binary=True, limit=100000)

    #KeyedVectors.intersect_word2vec_format()
    test = pd.read_csv('data\\ml-1m\\ratings_test_s.csv')


    word_list = []
    active_user_id = active_user
    testlist = list(test[test.userId == active_user_id]['movieId'])
    cnt = []
    rated_films = []

    for u_id, m_id, r, t in ratings.values:
        if u_id == active_user_id:
            m_id = (int(m_id))
            if m_id in list(i_dict.keys()):
                rated_films.append(m_id)
                if r > 3:
                    word_list.extend(nltk.word_tokenize(re.sub(r'[^\w\s]', '', i_dict[m_id])))

    cnt = [word for word in word_list if word not in stop_words]
    cnt = set(cnt)

    llist = [model[word] for word in cnt if word in model.key_to_index]
    #centroid_user = np.average([model[word] for word in set(nltk.word_tokenize(i_dict['1'])) if word in model])
    centroid_user = sum(llist)/len(llist)

    j_dict = {}
    for m_id in list(i_dict.keys()):
        tokens = set(nltk.word_tokenize(i_dict[m_id]))
        llist = [model[token] for token in tokens if token in model.key_to_index]
        if len(llist) != 0:
            j_dict[m_id] = sum(llist)/len(llist)

    similarity = {}
    for m_id in j_dict:
        if m_id not in rated_films:
            similarity[m_id] = 1 - spatial.distance.cosine(centroid_user, j_dict[m_id])

    sim = dict(sorted(similarity.items(), key=lambda item: item[1], reverse=True))

    for i in list(sim.keys())[:15]:
        liss = list(movies[movies.movieId == i]['title'].values)
        if len(liss) != 0:
            sim[i] = liss[0]
    dat = ""
    for i in list(sim.keys())[:15]:
        dat = dat + str(i) + "    " + str(sim[i]) + " \n"

    return dat

