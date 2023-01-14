# -*- coding: utf-8 -*-
"""
Created on Thu May  3 10:22:34 2018

@author: Frank
"""
from rec_fonction.EvaluationData import EvaluationData
from rec_fonction.EvaluatedAlgorithm import EvaluatedAlgorithm

class Evaluator:
    
    algorithms = []
    
    def __init__(self, dataset, rankings):
        ed = EvaluationData(dataset, rankings)
        self.dataset = ed
        
    def AddAlgorithm(self, algorithm, name):
        alg = EvaluatedAlgorithm(algorithm, name)
        self.algorithms.append(alg)
        
    def Evaluate(self, doTopN):
        results = {}
        for algorithm in self.algorithms:
            print("Evaluating ", algorithm.GetName(), "...")
            results[algorithm.GetName()] = algorithm.Evaluate(self.dataset, doTopN)

        # Print results
        print("\n")
        
        if (doTopN):
            print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(
                    "Algorithm", "RMSE", "MAE", "HR", "cHR", "ARHR", "Coverage", "Diversity", "Novelty"))
            for (name, metrics) in results.items():
                print("{:<10} {:<10.4f} {:<10.4f} {:<10.4f} {:<10.4f} {:<10.4f} {:<10.4f} {:<10.4f} {:<10.4f}".format(
                        name, metrics["RMSE"], metrics["MAE"], metrics["HR"], metrics["cHR"], metrics["ARHR"],
                                      metrics["Coverage"], metrics["Diversity"], metrics["Novelty"]))
        else:
            print("{:<10} {:<10} {:<10}".format("Algorithm", "RMSE", "MAE"))
            for (name, metrics) in results.items():
                print("{:<10} {:<10.4f} {:<10.4f}".format(name, metrics["RMSE"], metrics["MAE"]))
                
        print("\nLegend:\n")
        print("RMSE:      Root Mean Squared Error. Lower values mean better accuracy.")
        print("MAE:       Mean Absolute Error. Lower values mean better accuracy.")
        if (doTopN):
            print("HR:        Hit Rate; how often we are able to recommend a left-out rating. Higher is better.")
            print("cHR:       Cumulative Hit Rate; hit rate, confined to ratings above a certain threshold. Higher is better.")
            print("ARHR:      Average Reciprocal Hit Rank - Hit rate that takes the ranking into account. Higher is better." )
            print("Coverage:  Ratio of users for whom recommendations above a certain threshold exist. Higher is better.")
            print("Diversity: 1-S, where S is the average similarity score between every possible pair of recommendations")
            print("           for a given user. Higher means more diverse.")
            print("Novelty:   Average popularity rank of recommended items. Higher means more novel.")

    def SampleTopNRecs2(self, testSubject=85, k=10):

        i = 1
        svd_dict = dict()
        knndict = dict()
        for algo in self.algorithms:
            print("\nUsing recommender ", algo.GetName())

            print("\nBuilding recommendation model...")
            trainSet = self.dataset.GetFullTrainSet()
            algo.GetAlgorithm().fit(trainSet)

            print("Computing recommendations...")
            testSet = self.dataset.GetAntiTestSetForUser(testSubject)

            predictions = algo.GetAlgorithm().test(testSet)

            recommendations = []

            print("\nWe recommend:")
            for userID, movieID, actualRating, estimatedRating, _ in predictions:
                intMovieID = int(movieID)
                recommendations.append((intMovieID, estimatedRating))

            recommendations.sort(key=lambda x: x[1], reverse=True)

            for ratings in recommendations[:k]:
                if (i == 1):
                    knndict[ratings[0]] = ""
                else:
                    svd_dict[ratings[0]] = ""
            i = i + 1
        return knndict, svd_dict

    def topNrec(self, ml, testSubject=85, k=30):
        
        trainSet = self.dataset.GetFullTrainSet()
        self.algorithms[0].GetAlgorithm().fit(trainSet)
        testSet = self.dataset.GetAntiTestSetForUser(testSubject)
        predictions = self.algorithms[0].GetAlgorithm().test(testSet)
        
           
        recommendations = dict()
        print(type(recommendations))
        for userID, movieID, actualRating, estimatedRating, _ in predictions:
                
            intMovieID = int(movieID)
            recommendations[str(movieID)]=estimatedRating
        recommendation=dict(sorted(recommendations.items(), key=lambda item: item[1], reverse=True)) 
        print(type(recommendation))
     
        return recommendation
    def topNrec2(self, ml, testSubject=85, k=30):
        
        trainSet = self.dataset.GetFullTrainSet()
        self.algorithms[0].GetAlgorithm().fit(trainSet)
        testSet = self.dataset.GetAntiTestSetForUser(testSubject)
        predictions = self.algorithms[0].GetAlgorithm().test(testSet)
        
           
        recommendations = dict()
        print(type(recommendations))
        for userID, movieID, actualRating, estimatedRating, _ in predictions:
                
            intMovieID = int(movieID)
            recommendations[str(movieID)]=estimatedRating
        recommendation=dict(sorted(recommendations.items(), key=lambda item: item[1], reverse=True)) 
        print(type(recommendation))
        new_rec=dict()
        cpt=0
        for ratings in recommendation.keys():
                new_rec[ratings]=recommendation[ratings]
                cpt=cpt+1
                if cpt==k:
                    break
        print("len",len(new_rec))
        return new_rec

    def topNrec3(self, testSubject=85, k=30):

        trainSet = self.dataset.GetFullTrainSet()
        self.algorithms[0].GetAlgorithm().fit(trainSet)
        testSet = self.dataset.GetAntiTestSetForUser(testSubject)
        predictions = self.algorithms[0].GetAlgorithm().test(testSet)

        recommendations = dict()
        print(type(recommendations))
        for userID, movieID, actualRating, estimatedRating, _ in predictions:
            intMovieID = int(movieID)
            recommendations[str(movieID)] = estimatedRating
        recommendation = dict(sorted(recommendations.items(), key=lambda item: item[1], reverse=True))
        print(type(recommendation))
        new_rec = dict()
        cpt = 0
        for ratings in recommendation.keys():
            new_rec[ratings] = recommendation[ratings]
            cpt = cpt + 1
            if cpt == k:
                break
        print("len", len(new_rec))
        return new_rec
            
                
    def affichage(self,ml,i,s):
        trainSet = self.dataset.GetFullTrainSet()
        self.algorithms[0].GetAlgorithm().fit(trainSet)
        testSet = self.dataset.GetAntiTestSetForUser(i)
        predictions = self.algorithms[0].GetAlgorithm().test(testSet)
        #print(predictions[0])
        #if s==10:
            #print(predictions)
            #print(len(predictions))
        return predictions
    def precision(self,ml,k):
        user=[]
        trainSet = self.dataset.GetFullTrainSet()
        
        self.algorithms[0].GetAlgorithm().fit(trainSet)
        alltestset = self.dataset.GetTestSet()
        moyenne=0
        nbr=0
        print(alltestset[0])
        print(type(alltestset[0][1]))
        
        for idd,mon,rat in alltestset:
            
            if (idd not in user):
                user.append(idd)
                s=0
                
                test_subject_iid = trainset.to_inner_uid(idd)
                testSet = self.dataset.GetAntiTestSetForUser(test_subject_iid)
                predictions = self.algorithms[0].GetAlgorithm().test(testSet)
                print("ezeazeaze")
                predictions.sort(key=lambda x: x[3], reverse=True)
                print(predictions[0])
                for z in range(k):
                    if(predictions[z][1] in alltestset[1]):
                        s=s+1
                        print("ssss=",s)
                z=0
                    
                #if(len(predictions)>k):
                    #s=s+k
                #else:
                    #s=s+len(predictions)
                prec=s/k
                nbr=nbr+1
                moyenne=moyenne+prec
                print("user=",idd)
                print("precision",prec)
        print("islam")
        print(moyenne/nbr)

