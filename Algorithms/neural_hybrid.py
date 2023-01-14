from tensorflow.keras.layers import Embedding, Input, GlobalAveragePooling1D, Flatten, Multiply, Dense, Conv1D, \
    GlobalMaxPooling1D, Concatenate
from tensorflow.keras.models import Model, Sequential
from tensorflow.keras import activations
import pandas as pd
import math
import time
import json
import nltk
import numpy as np
from sklearn.model_selection import train_test_split



path = "C:\\Users\\USER\\PycharmProjects\\Recommender\\data\\ml-custom"
path2 = 'C:\\Users\\USER\\PycharmProjects\\Recommender'


def evaluate_model(model, test, k):
    test_userID = test['userId']
    test_movieID = test['movieId']
    test_movieText = test['movie_text']
    test_userText = test['user_info']

    arr = np.array(test_movieText.values.tolist())
    arr2 = np.array(test_userText.values.tolist())

    predictions = model.predict([test_userID, test_movieID, arr, arr2], verbose=2)

    predictions = pd.DataFrame(data=predictions, columns=['predicted'])
    predictions = pd.concat([test, predictions], axis=1)
    predictions = predictions.sort_values(by=['predicted'], ascending=False)

    users = test.userId.unique()

    hrs, ndcgs, hrms, rappels = 0, 0, 0, 0
    for u in users:
        p = predictions[predictions['userId'] == u].loc[:, 'rating'].head(k)
        nb_hits = len(predictions.loc[(predictions['userId'] == u) & (predictions['predicted'] > 0.5)])
        nb_predicted = len(predictions.loc[(predictions['userId'] == u) & (predictions['predicted'] > 0.5) & (
                    predictions['rating'] == 1)])
        hr, ndcg, hrm = evaluate_by_user(p, k)
        hrs = hrs + hr
        rappel = (hrm * k) / (nb_hits + 0.0000001)
        rappel = nb_predicted / (nb_hits + 0.0000001)
        ndcgs = ndcgs + ndcg
        hrms = hrms + hrm
        rappels = rappels + rappel

    mean_hr = hrs / len(users)
    mean_ndcg = ndcgs / len(users)
    mean_hrm = hrms / len(users)
    mean_rappel = rappels / len(users)

    return mean_hr, mean_ndcg, mean_hrm, mean_rappel


def evaluate_by_user(test, k):
    idcg = {10: 4.5432,
            15: 5.8608,
            20: 7.0395,
            30: 9.1567}

    hr, ndcg = 0, 0
    hrm = 0
    i = 1
    for rating in test:
        if rating == 1:
            hr = 1
            ndcg = ndcg + (1 / math.log2(i + 1))
            hrm = hrm + 1
        i = i + 1
    return hr, ndcg / idcg[k], hrm / (i - 1)


def affiche_tests_app2():
    from keras.preprocessing.text import Tokenizer
    from keras.preprocessing.sequence import pad_sequences
    from tensorflow import keras

    modell = keras.models.load_model("C:\\Users\\USER\\PycharmProjects\\Recommender\\data\\ml-custom\\model2")
    f = open(path2 + '\\movie_data.json', )
    data = json.load(f)

    data2 = pd.read_csv(path + '\\users.csv')

    sentences = data.values()
    sentences2 = data2[['gender', 'age', 'occupation']].values.tolist()

    tokenizer = Tokenizer(num_words=5000)
    tokenizer2 = Tokenizer(num_words=5000)
    tokenizer.fit_on_texts(sentences)
    tokenizer2.fit_on_texts(sentences2)

    X_train = tokenizer.texts_to_sequences(sentences)
    XX_train = tokenizer2.texts_to_sequences(sentences2)

    vocab_size = len(tokenizer.word_index) + 1
    vocab_size2 = len(tokenizer2.word_index) + 1

    maxlen = 60

    X_train = pad_sequences(X_train, padding='post', maxlen=maxlen)
    XX_train = pad_sequences(XX_train, padding='post', maxlen=3)

    movies = pd.read_csv(path + "\\movies.csv")
    users = pd.read_csv(path + "\\users.csv")

    texts = pd.DataFrame(columns=['movie_text'])
    user_info = pd.DataFrame(columns=['user_info'])

    a = list(X_train)
    b = list(XX_train)

    texts['movie_text'] = texts['movie_text'].astype(object)
    user_info['user_info'] = user_info['user_info'].astype(object)

    texts['movie_text'] = a
    user_info['user_info'] = b


    texts = pd.concat([movies, texts], axis=1)
    user_info = pd.concat([users, user_info], axis=1)


    testset = pd.read_csv(path + "\\ratings_test_sparse.csv")
    test = testset[:-1]

    test = texts[['movieId', 'movie_text']].merge(test, on='movieId', how='inner', suffixes=('_1', '_2'))
    test = user_info[['userId', 'user_info']].merge(test, on='userId', how='inner', suffixes=('_1', '_2'))


    results = []
    for i in [10, 15, 20, 30]:
        hr, ndcg, hrm, rappel = evaluate_model(modell, test, i)
        results.append((hrm, ndcg))
    return results

def affiche_list_app2(active_user):
    from keras.preprocessing.text import Tokenizer
    from keras.preprocessing.sequence import pad_sequences
    from tensorflow import keras

    modell = keras.models.load_model("C:\\Users\\USER\\PycharmProjects\\Recommender\\data\\ml-custom\\model2")
    f = open(path2 + '\\movie_data.json', )
    data = json.load(f)

    data2 = pd.read_csv(path + '\\users.csv')

    sentences = data.values()
    sentences2 = data2[['gender', 'age', 'occupation']].values.tolist()

    tokenizer = Tokenizer(num_words=5000)
    tokenizer2 = Tokenizer(num_words=5000)
    tokenizer.fit_on_texts(sentences)
    tokenizer2.fit_on_texts(sentences2)

    X_train = tokenizer.texts_to_sequences(sentences)
    XX_train = tokenizer2.texts_to_sequences(sentences2)

    vocab_size = len(tokenizer.word_index) + 1
    vocab_size2 = len(tokenizer2.word_index) + 1

    maxlen = 60

    X_train = pad_sequences(X_train, padding='post', maxlen=maxlen)
    XX_train = pad_sequences(XX_train, padding='post', maxlen=3)

    movies = pd.read_csv(path + "\\movies.csv")
    users = pd.read_csv(path + "\\users.csv")

    texts = pd.DataFrame(columns=['movie_text'])
    user_info = pd.DataFrame(columns=['user_info'])

    a = list(X_train)
    b = list(XX_train)

    texts['movie_text'] = texts['movie_text'].astype(object)
    user_info['user_info'] = user_info['user_info'].astype(object)

    texts['movie_text'] = a
    user_info['user_info'] = b

    texts = pd.concat([movies, texts], axis=1)
    user_info = pd.concat([users, user_info], axis=1)

    testset = pd.read_csv(path + "\\ratings_test_sparse.csv")
    test = testset[:-1]

    test = texts[['movieId', 'movie_text']].merge(test, on='movieId', how='inner', suffixes=('_1', '_2'))
    test = user_info[['userId', 'user_info']].merge(test, on='userId', how='inner', suffixes=('_1', '_2'))

    test_userID = test['userId']
    test_movieID = test['movieId']
    test_movieText = test['movie_text']
    test_userText = test['user_info']

    arr = np.array(test_movieText.values.tolist())
    arr2 = np.array(test_userText.values.tolist())

    predictions = modell.predict([test_userID, test_movieID, arr, arr2], verbose=2)

    predictions = pd.DataFrame(data=predictions, columns=['predicted'])
    predictions = pd.concat([test, predictions], axis=1)
    predictions = predictions.sort_values(by=['predicted'], ascending=False)
    pp = predictions.loc[predictions['userId'] == active_user, ['rating', 'predicted', 'movieId']].head(15)
    sim = {}
    for l in list(pp['movieId']):
        sim[l] = ''
    for i in list(sim.keys())[:15]:
        liss = list(movies[movies.movieId == i]['title'].values)
        if len(liss) != 0:
            sim[i] = liss[0]
    dat = ""
    for i in list(sim.keys())[:15]:
        dat = dat + str(i) + "    " + str(sim[i]) + " \n"

    return dat
