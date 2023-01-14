
import pandas as pd
import math
import time
import json
import nltk
import numpy as np
from sklearn.model_selection import train_test_split


path = "C:\\Users\\USER\\PycharmProjects\\Recommender\\data\\ml-custom"
path2 = 'C:\\Users\\USER\\PycharmProjects\\Recommender'


def build_model(emb_size_id, emb_size_text, maxlength, nbl ,nbn):
    import keras
    from keras.preprocessing.text import Tokenizer
    from keras.preprocessing.sequence import pad_sequences
    from tensorflow.keras.layers import Embedding, Input, GlobalAveragePooling1D, Flatten, Multiply, Dense, Conv1D, \
        GlobalMaxPooling1D, Concatenate
    from tensorflow.keras.models import Model, Sequential
    from tensorflow.keras import activations
    f = open(path2 + '\\movie_data2.json', )
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
    maxlen = maxlength

    print(vocab_size2)

    X_train = pad_sequences(X_train, padding='post', maxlen=maxlen)
    XX_train = pad_sequences(XX_train, padding='post', maxlen=3)

    input_movieText = Input(shape=[maxlen], name='itemText')
    input_userText = Input(shape=[3], name='userText')
    input_userID = Input(shape=[1], name='userID')
    input_movieID = Input(shape=[1], name='movieID')

    user_emb = Embedding(6040, emb_size_id, name='user_emb')(input_userID)
    movie_emb = Embedding(3953, emb_size_id, name='movie_emb')(input_movieID)

    flat_user = Flatten()(user_emb)
    flat_movie = Flatten()(movie_emb)

    embedding_dim = emb_size_text

    conc_layer = Concatenate()([flat_user, input_userText])

    text_emb = Embedding(vocab_size, embedding_dim)(input_movieText)
    text_conv = Conv1D(emb_size_id, 5, activation='relu')(text_emb)
    text_pool = GlobalAveragePooling1D()(text_conv)

    encoder = keras.models.load_model('C:\\Users\\USER\\PycharmProjects\\Recommender\\data\\ml-custom\\model3')


    mul_layer = Multiply()([flat_movie, text_pool])
    activ_layer = activations.tanh(mul_layer)

    conc_layer2 = Concatenate()([activ_layer, conc_layer])

    mlp_layer = Dense(nbn, activation='relu')(conc_layer2)
    for i in range(nbl - 1):
        mlp_layer = Dense(nbn, activation='relu')(mlp_layer)

    out = Dense(1, activation='sigmoid', name='output')(mlp_layer)

    NCTR_model = Model([input_userID, input_movieID, input_movieText, input_userText], out)

    return NCTR_model, X_train, XX_train


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

    print(predictions.loc[predictions['userId'] == 702, ['rating', 'predicted']].head(k))

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


def train(model, trains, X_train, XX_train, test, num_epochs, batch):
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

    trains = texts[['movieId', 'movie_text']].merge(trains, on='movieId', how='inner', suffixes=('_1', '_2'))
    test = texts[['movieId', 'movie_text']].merge(test, on='movieId', how='inner', suffixes=('_1', '_2'))

    trains = user_info[['userId', 'user_info']].merge(trains, on='userId', how='inner', suffixes=('_1', '_2'))
    test = user_info[['userId', 'user_info']].merge(test, on='userId', how='inner', suffixes=('_1', '_2'))

    train_userID = trains['userId']
    train_movieID = trains['movieId']
    train_movieText = trains['movie_text']
    train_userText = trains['user_info']
    train_y = trains['rating']

    arr = np.array(train_movieText.values.tolist())
    arr2 = np.array(train_userText.values.tolist())

    print('\nTRAINING ' + '...\n')

    # intitialisation
    print(test)
    best_hr, best_ndcg, best_hrm, rappel = evaluate_model(model, test, 10)

    best_iteration = 0
    all_hrs, all_ndcgs = {}, {}
    all_hrs[0], all_ndcgs[0] = best_hr, best_ndcg

    for epoch in range(1, num_epochs + 1):

        history = model.fit([train_userID, train_movieID, arr, arr2], train_y, batch_size=batch, epochs=1, verbose=1,
                            shuffle=True)

        results = []
        for i in [10, 15, 20, 30]:
            hr, ndcg, hrm, rappel = evaluate_model(model, test, i)
            results.append((hrm, ndcg))

        if ndcg > best_ndcg:
            best_hr, best_ndcg, best_iteration = hr, ndcg, epoch
            bad_epochs = 0

        print('Iteration %d : loss = %.4f, HR = %.4f, NDCG = %.4f, Précision = %.4f, Rappel = %.4f' % (
            epoch, history.history['loss'][0], hr, ndcg, hrm, rappel))
        print(history.history['accuracy'])
        #model.save(path + "\\model" + str(epoch))

    print("Best iteration %d, best HR = %.4f, best NDCG = %.4f" % (best_iteration, best_hr, best_ndcg))

    return results

def affiche_tests_train(nbl, nbn):

    trainset = pd.read_csv(path + "\\ratings_train_sparse.csv")
    testset = pd.read_csv(path + "\\ratings_test_sparse.csv")


    NCTR, X_train, XX_train = build_model(70, 100, 60, int(nbl), int(nbn))
    NCTR.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    results = train(NCTR, trainset, X_train, XX_train, testset[:-1], 1, 100)
    return results
