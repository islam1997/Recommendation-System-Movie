#from MovieLens import MovieLens
from surprise import KNNBasic
from surprise import NormalPredictor
#from Evaluator import Evaluator
from surprise import SVD, SVDpp
import random
import json
import pandas as pd
import os.path
from rec_fonction.MovieLens import MovieLens
from rec_fonction.Evaluator import Evaluator

from surprise.model_selection import KFold
import copy


#from surprise import NormalPredictor
from surprise.model_selection import KFold
import math

import random
import numpy as np

movies = pd.read_csv("C:\\Users\\USER\\PycharmProjects\\Recommender\\data\\ml-1m\\movies.csv")
class Algo_hybrid():
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
        
    def hybridation(self,algo1,algo2,k_nn):
        if(algo1=='knn'):
            UserKNN=KNNBasic(k_nn,1,sim_options={'name':'cosine','user_based':True})
            self.evaluator.AddAlgorithm(UserKNN,"User KNN")
        else:
            svd=SVD()
            self.evaluator.AddAlgorithm(svd,"SVD")
        #print(p)
        new_dict_est=dict()
        list_of_predect=[]
        list_of_user=["10","33","36","48","53","58","62","117","123","146"]
        alpha=0.1
        beta=1
        #p=evaluator.affichage(ml,int(list_of_user[0]),10)
        Dict=dict()
        Dict2=dict()
        tp = 0
        tn = 0
        hh = 0
        test = pd.read_csv('data\\ml-1m\\ratings_test_s.csv')
        ids = list(test.userId.unique())[:100]
        Dict.clear()

        for idd in ids:

 
           List=[]
           alpha=0.1
           beta=1
           #Dict2.clear()
           #Dict2.clear()
           #print("islam2")
           A=1
           Dict.clear()
           Dict2.clear()
           #test_subject='889'
           #test_subject_iid = trainset.to_inner_uid(test_subject)
           p=self.evaluator.topNrec(self.ml,idd,200)
           while(alpha<=0.9):

               #index_file = open("C:/tmp/alpha_"+str(A)+"_"+str(idd)+".json", "w")
               #print(type(p))
               if(algo2=='vect'):
                   index_file = open("C:\\Users\\USER\\PycharmProjects\\Recommender\\vect_LOD\\vect" + str(idd) + ".json", "r")
               else:
                   index_file = open("C:\\Users\\USER\\PycharmProjects\\Recommender\\w2v\\w2v" + str(idd) + ".json", "r")



               dict_ml= json.load(index_file)
               list_of_predect=[]
               #print(p)
               # #p=evaluator.topNrec(ml,idd,30)
               for e in p.keys():
                   p[e]=p[e]/5
                   if e in dict_ml:
                       Dict[e]=p[e]
                       Dict2[e]=dict_ml[e]
                       list_of_predect.append(p[e])

                #print("islz",type(Dict.values))
               for f in Dict.keys():
                   Dict[f]=Dict[f]*alpha
                   Dict2[f]=Dict2[f]*beta
                   Dict[f]=(Dict[f]+Dict2[f])
               if(algo1=='knn' and algo2=='vect'):
                   index_file = open("C:\\Users\\USER\\PycharmProjects\\Recommender\\new_vect_knn\\alpha_" + str(A) + "_" + str(idd) + ".json", "w")
               if(algo1=='svd' and algo2=='vect'):
                   index_file = open("C:\\Users\\USER\\PycharmProjects\\Recommender\\new_vect_svd\\alpha_" + str(A) + "_" + str(idd) + ".json", "w")
               if (algo1 == 'svd' and algo2 == 'w2v'):
                   index_file = open("C:\\Users\\USER\\PycharmProjects\\Recommender\\new_w2v_svd\\alpha_" + str(A) + "_" + str(idd) + ".json", "w")
               if (algo1 == 'knn' and algo2 == 'w2v'):
                   index_file = open("C:\\Users\\USER\\PycharmProjects\\Recommender\\new_w2v_knn\\alpha_" + str(A) + "_" + str(idd) + ".json", "w")

               A=A+1
               json.dump(Dict, index_file)
               index_file.close()
               alpha=alpha+0.1
               #print("islam4")
               #print(Dict)
               #print(List[0])
               beta=beta-0.1
        index_file.close()

    def hybridation2(self, algo1, algo2, k_nn,new_alpha, uid):
        new_alpha = int(new_alpha)
        if (algo1 == 'knn'):
            UserKNN = KNNBasic(k_nn, 1, sim_options={'name': 'cosine', 'user_based': True})
            self.evaluator.AddAlgorithm(UserKNN, "User KNN")
        else:
            svd = SVD()
            self.evaluator.AddAlgorithm(svd, "SVD")
        # print(p)
        new_dict_est = dict()
        list_of_predect = []
        list_of_user = ["10", "33", "36", "48", "53", "58", "62", "117", "123", "146"]
        alpha = new_alpha
        beta = 1
        # p=evaluator.affichage(ml,int(list_of_user[0]),10)
        Dict = dict()
        Dict2 = dict()
        tp = 0
        tn = 0
        hh = 0
        test = pd.read_csv('C:\\Users\\USER\\PycharmProjects\\Recommender\\data\\ml-1m\\ratings_test_s.csv')
        ids = [uid]
        Dict.clear()

        for idd in ids:

            List = []
            #alpha = 0.1
            beta = 1
            # Dict2.clear()
            # Dict2.clear()
            # print("islam2")
            A = 1
            Dict.clear()
            Dict2.clear()
            # test_subject='889'
            # test_subject_iid = trainset.to_inner_uid(test_subject)
            p = self.evaluator.topNrec(self.ml, idd, 200)

            if (algo2 == 'vect'):
                index_file = open("C:\\Users\\USER\\PycharmProjects\\Recommender\\vect\\vect" + str(idd) + ".json",
                                    "r")
            if (algo2 == 'vect_lod'):
                index_file = open(
                    "C:\\Users\\USER\\PycharmProjects\\Recommender\\vect_LOD\\vect" + str(idd) + ".json", "r")
            if (algo2 == 'w2v'):
                index_file = open("C:\\Users\\USER\\PycharmProjects\\Recommender\\w2v\\w2v" + str(idd) + ".json",
                                    "r")
            if (algo2 == 'w2v_lod'):
                index_file = open("C:\\Users\\USER\\PycharmProjects\\Recommender\\w2v_LOD\\w2v" + str(idd) + ".json",
                                    "r")
            if (algo2 == 'ml'):
                index_file = open("C:\\Users\\USER\\PycharmProjects\\Recommender\\ml\\ml" + str(idd) + ".json",
                                    "r")
            if (algo2 == 'ml_lod'):
                index_file = open("C:\\Users\\USER\\PycharmProjects\\Recommender\\ml_LOD\\ml" + str(idd) + ".json",
                                    "r")


            dict_ml = json.load(index_file)
            list_of_predect = []
            # print(p)
            # #p=evaluator.topNrec(ml,idd,30)
            for e in p.keys():
                if e in dict_ml:
                    Dict[e] = p[e]
                    Dict2[e] = dict_ml[e]
                    list_of_predect.append(p[e])

            # print("islz",type(Dict.values))
            for f in Dict.keys():
                Dict[f] = Dict[f] * alpha
                Dict2[f] = Dict2[f] * beta
                #hada dict li dirlo trie Dict[f]
                Dict[f] = (Dict[f] + Dict2[f]) / 5
            similarity = dict(sorted(Dict.items(), key=lambda item: item[1], reverse=True))
        return similarity












    def call_precesion_ngcd_lod_vect(self,fichier,al,number_u):
        
        test = pd.read_csv('C:\\Users\\USER\\PycharmProjects\\Recommender\\data\\ml-1m\\ratings_test_s.csv')
        ids = list(test.userId.unique())[:number_u]
        print(ids)
        tp = 0
        tn = 0
        hh = 0
        idcg = {10: 4.5432,
        15: 5.8608,
        20: 7.0395,
        30: 9.1567}
        #nbr = 10
        cpt=0
        List_tuple=[]
        kf = KFold(n_splits=2)
        #List_resultat=[]
        list_k=[10,15,20,30]
        for i in range(4):
            tp = 0
            tn = 0
            for trainset, testset in kf.split(self.evaluationData):
                z=0
                Liste=[]
                for idd in ids:
                    z=z+1
                    active_user_id = idd
                    testlist = list(test[test.userId == active_user_id]['movieId'])
                    filename = "C:\\Users\\USER\\PycharmProjects\\Recommender\\"+fichier+"\\alpha_"+str(al)+"_"+ str(idd)+ ".json"
                    if os.path.isfile(filename):
                        cpt=cpt+1
                        #print(cpt)
                        #print(testlist)
                        ff = open(filename)
                        recommandation = json.load(ff)
                        recommandation = dict(sorted(recommandation.items(), key=lambda item: item[1], reverse=True))
                        recommandations = [int(key) for key in recommandation.keys()][:list_k[i]]
                        nb = 0
                        cnt = 0
                        ndcg = 0
                        for ii in recommandations:
                            cnt = cnt + 1
                            for j in testlist:
                                if ii == j:
                                    nb = nb + 1
                                    ndcg = ndcg + (1 / math.log2(cnt + 1))
                        ndcg = ndcg / idcg[list_k[i]]
                                            
                        tp = tp + ((nb / list_k[i]) * len(test[test.userId == active_user_id]))
                        tn = tn + (ndcg * len(test[test.userId == active_user_id]))
                        print(tp, ' ', active_user_id)
                    else:
                        print("file dosent exist")
            List_tuple.append((tp / (len(test[test['userId'].isin(ids)])),tn / (len(test[test['userId'].isin(ids)]))))
        return List_tuple
            
    def call_precesion_ngcd_w2v(self,fichier,al, number_u):
        test = pd.read_csv('C:\\Users\\USER\\PycharmProjects\\Recommender\\data\\ml-1m\\ratings_test_s.csv')
        ids = list(test.userId.unique())[:number_u]
        #print(ids)

        idcg = {10: 4.5432,
        15: 5.8608,
        20: 7.0395,
        30: 9.1567}
        nbr = 10
        cpt=0
        Liste=[]
        z=0
        List_tuple=[]
        list_k=[10,15,20,30]
        for i in range(4):
            tp = 0
            tn = 0
            for idd in ids:
               z=z+1
               active_user_id = idd
               testlist = list(test[test.userId == active_user_id]['movieId'])
               #print(testlist)
               filename = "C:\\Users\\USER\\PycharmProjects\\Recommender\\"+fichier+"\\alpha_"+str(al)+"_"+str(idd)+".json"
               if os.path.isfile(filename):

                  cpt=cpt+1
                  print(cpt)
                  ff = open(filename)
                  recommandation = json.load(ff)
                  recommandation = dict(sorted(recommandation.items(), key=lambda item: item[1], reverse=True))
                  recommandations = [int(key) for key in recommandation.keys()][:list_k[i]]
                  #print(recommandations)
                  nb = 0
                  cnt = 0
                  ndcg = 0
                  for ii in recommandations:
                      cnt = cnt + 1
                      for j in testlist:
                          if ii == j:
                              nb = nb + 1
                              ndcg = ndcg + (1 / math.log2(cnt + 1))
                  ndcg = ndcg / idcg[list_k[i]]

                  tp = tp + ((nb / list_k[i]) * len(test[test.userId == active_user_id]))
                  tn = tn + (ndcg * len(test[test.userId == active_user_id]))
                  print(tp, ' ', active_user_id)
               else:
                  print("file dosent exist")
            List_tuple.append((tp / (len(test[test['userId'].isin(ids)])),tn / (len(test[test['userId'].isin(ids)]))))
        return List_tuple

def affiche_tests_hyb_w2v_knn(nbu, alpha):
    algo = Algo_hybrid()
    algo.eval()
    return algo.call_precesion_ngcd_w2v('new_w2v_knn', alpha, nbu)
def affiche_tests_hyb_w2v_svd(nbu, alpha):
    algo = Algo_hybrid()
    algo.eval()
    return algo.call_precesion_ngcd_w2v('new_w2v_svd', alpha, nbu)
def affiche_tests_hyb_w2v_LOD_knn(nbu, alpha):
    algo = Algo_hybrid()
    algo.eval()
    return algo.call_precesion_ngcd_w2v('new_w2v_lod_knn', alpha, nbu)
def affiche_tests_hyb_w2v_LOD_svd(nbu, alpha):
    algo = Algo_hybrid()
    algo.eval()
    return algo.call_precesion_ngcd_w2v('new_w2v_lod_svd', alpha, nbu)
def affiche_tests_hyb_vect_knn(nbu, alpha):
    algo = Algo_hybrid()
    algo.eval()
    return algo.call_precesion_ngcd_lod_vect('new_vect_NO_knn', alpha, nbu)
def affiche_tests_hyb_vect_lod_knn(nbu, alpha):
    algo = Algo_hybrid()
    algo.eval()
    return algo.call_precesion_ngcd_lod_vect('new_vect_knn', alpha, nbu)

def affiche_tests_hyb_vect_svd(nbu, alpha):
    algo = Algo_hybrid()
    algo.eval()
    return algo.call_precesion_ngcd_lod_vect('new_vect_NO_svd', alpha, nbu)
def affiche_tests_hyb_vect_lod_svd(nbu, alpha):
    algo = Algo_hybrid()
    algo.eval()
    return algo.call_precesion_ngcd_lod_vect('new_vect_svd', alpha, nbu)
def affiche_tests_hyb_ml_svd(nbu, alpha):
    algo = Algo_hybrid()
    algo.eval()
    return algo.call_precesion_ngcd_lod_vect('new_ml_svd', alpha, nbu)
def affiche_tests_hyb_ml_lod_svd(nbu, alpha):
    algo = Algo_hybrid()
    algo.eval()
    return algo.call_precesion_ngcd_lod_vect('new_ml_lod_svd', alpha, nbu)
def affiche_tests_hyb_ml_knn(nbu, alpha):
    algo = Algo_hybrid()
    algo.eval()
    return algo.call_precesion_ngcd_lod_vect('new_ml_knn', alpha, nbu)
def affiche_tests_hyb_ml_lod_knn(nbu, alpha):
    algo = Algo_hybrid()
    algo.eval()
    return algo.call_precesion_ngcd_lod_vect('new_ml_lod_knn', alpha, nbu)


def affiche_list_hyb_vect_lod_knn(idu, alpha):
    algo = Algo_hybrid()
    algo.eval()
    sim = algo.hybridation2('knn', 'vect_lod', 30, alpha, idu)
    for i in list(sim.keys())[:15]:
        liss = list(movies[movies.movieId == int(i)]['title'].values)
        if len(liss) != 0:
            sim[i] = liss[0]
    dat = ""
    for i in list(sim.keys())[:15]:
        dat = dat + str(i) + "    " + str(sim[i]) + " \n"

    return dat

def affiche_list_hyb_vect_lod_svd(idu, alpha):
    algo = Algo_hybrid()
    algo.eval()
    sim = algo.hybridation2('svd', 'vect_lod', 0, alpha, idu)
    for i in list(sim.keys())[:15]:
        liss = list(movies[movies.movieId == int(i)]['title'].values)
        if len(liss) != 0:
            sim[i] = liss[0]
    dat = ""
    for i in list(sim.keys())[:15]:
        dat = dat + str(i) + "    " + str(sim[i]) + " \n"

    return dat


def affiche_list_hyb_vect_knn(idu, alpha):
    algo = Algo_hybrid()
    algo.eval()
    sim = algo.hybridation2('knn', 'vect', 30, alpha, idu)
    for i in list(sim.keys())[:15]:
        liss = list(movies[movies.movieId == int(i)]['title'].values)
        if len(liss) != 0:
            sim[i] = liss[0]
    dat = ""
    for i in list(sim.keys())[:15]:
        dat = dat + str(i) + "    " + str(sim[i]) + " \n"

    return dat


def affiche_list_hyb_vect_svd(idu, alpha):
    algo = Algo_hybrid()
    algo.eval()
    sim = algo.hybridation2('svd', 'vect', 0, alpha, idu)
    for i in list(sim.keys())[:15]:
        liss = list(movies[movies.movieId == int(i)]['title'].values)
        if len(liss) != 0:
            sim[i] = liss[0]
    dat = ""
    for i in list(sim.keys())[:15]:
        dat = dat + str(i) + "    " + str(sim[i]) + " \n"

    return dat


def affiche_list_hyb_w2v_lod_knn(idu, alpha):
    algo = Algo_hybrid()
    algo.eval()
    sim = algo.hybridation2('knn', 'w2v_lod', 30, alpha, idu)
    for i in list(sim.keys())[:15]:
        liss = list(movies[movies.movieId == int(i)]['title'].values)
        if len(liss) != 0:
            sim[i] = liss[0]
    dat = ""
    for i in list(sim.keys())[:15]:
        dat = dat + str(i) + "    " + str(sim[i]) + " \n"

    return dat


def affiche_list_hyb_w2v_lod_svd(idu, alpha):
    algo = Algo_hybrid()
    algo.eval()
    sim = algo.hybridation2('svd', 'w2v_lod', 0, alpha, idu)
    for i in list(sim.keys())[:15]:
        liss = list(movies[movies.movieId == int(i)]['title'].values)
        if len(liss) != 0:
            sim[i] = liss[0]
    dat = ""
    for i in list(sim.keys())[:15]:
        dat = dat + str(i) + "    " + str(sim[i]) + " \n"

    return dat


def affiche_list_hyb_w2v_knn(idu, alpha):
    algo = Algo_hybrid()
    algo.eval()
    sim = algo.hybridation2('knn', 'w2v', 30, alpha, idu)
    for i in list(sim.keys())[:15]:
        liss = list(movies[movies.movieId == int(i)]['title'].values)
        if len(liss) != 0:
            sim[i] = liss[0]
    dat = ""
    for i in list(sim.keys())[:15]:
        dat = dat + str(i) + "    " + str(sim[i]) + " \n"

    return dat


def affiche_list_hyb_w2v_svd(idu, alpha):
    algo = Algo_hybrid()
    algo.eval()
    sim = algo.hybridation2('svd', 'w2v', 0, alpha, idu)
    for i in list(sim.keys())[:15]:
        liss = list(movies[movies.movieId == int(i)]['title'].values)
        if len(liss) != 0:
            sim[i] = liss[0]
    dat = ""
    for i in list(sim.keys())[:15]:
        dat = dat + str(i) + "    " + str(sim[i]) + " \n"

    return dat

def affiche_list_hyb_ml_lod_knn(idu, alpha):
    algo = Algo_hybrid()
    algo.eval()
    sim = algo.hybridation2('knn', 'ml_lod', 30, alpha, idu)
    for i in list(sim.keys())[:15]:
        liss = list(movies[movies.movieId == int(i)]['title'].values)
        if len(liss) != 0:
            sim[i] = liss[0]
    dat = ""
    for i in list(sim.keys())[:15]:
        dat = dat + str(i) + "    " + str(sim[i]) + " \n"

    return dat


def affiche_list_hyb_ml_lod_svd(idu, alpha):
    algo = Algo_hybrid()
    algo.eval()
    sim = algo.hybridation2('svd', 'ml_lod', 0, alpha, idu)
    for i in list(sim.keys())[:15]:
        liss = list(movies[movies.movieId == int(i)]['title'].values)
        if len(liss) != 0:
            sim[i] = liss[0]
    dat = ""
    for i in list(sim.keys())[:15]:
        dat = dat + str(i) + "    " + str(sim[i]) + " \n"

    return dat


def affiche_list_hyb_ml_knn(idu, alpha):
    algo = Algo_hybrid()
    algo.eval()
    sim = algo.hybridation2('knn', 'ml', 30, alpha, idu)
    for i in list(sim.keys())[:15]:
        liss = list(movies[movies.movieId == int(i)]['title'].values)
        if len(liss) != 0:
            sim[i] = liss[0]
    dat = ""
    for i in list(sim.keys())[:15]:
        dat = dat + str(i) + "    " + str(sim[i]) + " \n"

    return dat


def affiche_list_hyb_ml_svd(idu, alpha):
    algo = Algo_hybrid()
    algo.eval()
    sim = algo.hybridation2('svd', 'ml', 0, alpha, idu)
    for i in list(sim.keys())[:15]:
        liss = list(movies[movies.movieId == int(i)]['title'].values)
        if len(liss) != 0:
            sim[i] = liss[0]
    dat = ""
    for i in list(sim.keys())[:15]:
        dat = dat + str(i) + "    " + str(sim[i]) + " \n"

    return dat

