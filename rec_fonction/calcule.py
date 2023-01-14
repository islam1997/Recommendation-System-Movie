
from collections import defaultdict
from surprise import KNNBasic
from surprise import SVD
from rec_fonction.MovieLens import MovieLens
import pandas as pd


#from surprise import NormalPredictor
from surprise.model_selection import KFold
import math

import random
import numpy as np
from rec_fonction.Evaluator import Evaluator

movies = pd.read_csv("C:\\Users\\USER\\PycharmProjects\\Recommender\\data\\ml-1m\\movies.csv")

class Algo():
    def __init__(self):
        self.evaluator=None
        self.ml=None
        self.evaluationData=None
        self.rankings=None


    def LoadMovieLensData(self):
        ml = MovieLens()
        print("Loading movie ratings...")
        data = ml.loadMovieLensLatestSmall()
        print("\nComputing movie popularity ranks so we can measure novelty later...")
        rankings = ml.getPopularityRanks()
        return (ml, data, rankings)


    def eval(self):
        np.random.seed(0)
        random.seed(0)

        # Load up common data set for the recommender algorithms
        (self.ml, self.evaluationData, self.rankings) = self.LoadMovieLensData()
        # Construct an Evaluator to, you know, evaluate them
        
        self.evaluator= Evaluator(self.evaluationData, self.rankings)
        

    def precision_recall_at_k(self,predictions, k=30, threshold=3.5, number_of_user=102):
        
    

    # First map the predictions to each user.
        user_est_true = defaultdict(list)
    #print(predictions)
        cpt=1
        for uid, _, true_r, est, _ in predictions:
            
            user_est_true[uid].append((est, true_r))
    #print(len(user_est_true.keys()))
        user_est_true2 = defaultdict(list)
        for user in user_est_true.keys():
            user_est_true2[user]=user_est_true[user]
            if(cpt==number_of_user):
                break
            cpt=cpt+1
    #print(cpt)
        
        
        precisions = dict()
        recalls = dict()
        pos=1
        for uid, user_ratings in user_est_true2.items():
            
        
            # Sort user ratings by estimated value
            user_ratings.sort(key=lambda x: x[0], reverse=True)

            # Number of relevant items
            n_rel = sum((true_r >= threshold) for (_, true_r) in user_ratings)

            # Number of recommended items in top k
            n_rec_k = sum((est >= threshold) for (est, _) in user_ratings[:k])

            # Number of relevant and recommended items in top k
            n_rel_and_rec_k = sum(((true_r >= threshold) and (est >= threshold))
                              for (est, true_r) in user_ratings[:k])

            # Precision@K: Proportion of recommended items that are relevant
            # When n_rec_k is 0, Precision is undefined. We here set it to 0.

            precisions[uid] = n_rel_and_rec_k / n_rec_k if n_rec_k != 0 else 0

            # Recall@K: Proportion of relevant items that are recommended
            # When n_rel is 0, Recall is undefined. We here set it to 0.

            recalls[uid] = 1 / math.log2(n_rec_k+1) if n_rec_k != 0 else 0

        return precisions, recalls


    def calcule_svd(self,numberofuser=30):
        svd = SVD()
        self.evaluator.AddAlgorithm(svd, "SVD")
        kf = KFold(n_splits=4)
        cpt=numberofuser
        List_prec=[]
        List_ngcd=[]
        List_tuple=[]
       
        list_k=[10,15,20,30]
        for i in range(4):
            for trainset, testset in kf.split(self.evaluationData):
                svd.fit(trainset)
                predictions = svd.test(testset)
                precisions, recalls = self.precision_recall_at_k(predictions, list_k[i], threshold=4, number_of_user=cpt)
                List_prec.append(sum(prec for prec in precisions.values()) / len(precisions))
                List_ngcd.append(sum(rec for rec in recalls.values()) / len(recalls))
            List_tuple.append((sum(List_prec) / len(List_prec),sum(List_ngcd) / len(List_ngcd)))
            
        return List_tuple


    def calcule_knn(self,numberofuser=30,k_knn=20):
        UserKNN = KNNBasic(k_knn,1,sim_options = {'name': 'cosine', 'user_based': True})
        UserKNN = KNNBasic(sim_options = {'name': 'cosine', 'user_based': True})
        self.evaluator.AddAlgorithm(UserKNN, "User KNN")
        kf = KFold(n_splits=4)
        cpt=numberofuser
        List_prec=[]
        List_ngcd=[]
        List_tuple=[]
       
        list_k=[10,15,20,30]
        for i in range(4):
            for trainset, testset in kf.split(self.evaluationData):
                UserKNN.fit(trainset)
                predictions = UserKNN.test(testset)
                precisions, recalls = self.precision_recall_at_k(predictions, list_k[i], threshold=4, number_of_user=cpt)
                List_prec.append(sum(prec for prec in precisions.values()) / len(precisions))
                List_ngcd.append(sum(rec for rec in recalls.values()) / len(recalls))
            List_tuple.append((sum(List_prec) / len(List_prec),sum(List_ngcd) / len(List_ngcd)))
            
        return List_tuple




def affiche_tests_knn(nbu, k):
    algo=Algo()
    algo.eval()
    return algo.calcule_knn(nbu, k)

def affiche_tests_svd(nbu):
    algo = Algo()
    algo.eval()
    return algo.calcule_svd(nbu)

def affiche_lists_knn(idu, k):
    algo = Algo()
    algo.eval()
    UserKNN = KNNBasic(k, 1, sim_options={'name': 'cosine', 'user_based': True})
    algo.evaluator.AddAlgorithm(UserKNN, "User KNN")
    svd = SVD()
    algo.evaluator.AddAlgorithm(svd, "SVD")
    sim, sim2 = algo.evaluator.SampleTopNRecs2(idu, 15)
    for i in list(sim.keys()):
        liss = list(movies[movies.movieId == int(i)]['title'].values)
        if len(liss) != 0:
            sim[i] = liss[0]
    dat = ""
    for i in list(sim.keys()):
        dat = dat + str(i) + "    " + str(sim[i]) + " \n"


    return dat

def affiche_lists_svd(idu):
    algo = Algo()
    algo.eval()
    UserKNN = KNNBasic(sim_options={'name': 'cosine', 'user_based': True})
    algo.evaluator.AddAlgorithm(UserKNN, "User KNN")
    svd = SVD()
    algo.evaluator.AddAlgorithm(svd, "SVD")
    sim, sim2 = algo.evaluator.SampleTopNRecs2(idu, 15)

    for i in list(sim2.keys()):
        liss = list(movies[movies.movieId == int(i)]['title'].values)
        if len(liss) != 0:
            sim2[i] = liss[0]

    dat2 = ""
    for i in list(sim2.keys()):
        dat2 = dat2 + str(i) + "    " + str(sim2[i]) + " \n"

    return dat2






