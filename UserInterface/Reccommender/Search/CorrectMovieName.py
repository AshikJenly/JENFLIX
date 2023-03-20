import numpy as np
import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class MovieName():
    def __init__(self):
        try:
            df=pd.read_csv('static/DATASETS/Final_movie.csv',index_col=0)
            self.__movies=list(df['title'])
            self.__cv=CountVectorizer(max_features=5000,stop_words='english')
        except:
            print("Error in MovieName in CorrectMovieName file")
    def get_appropriate_name(self,movie):
        self.__movies.insert(0,movie)
        vector=self.__cv.fit_transform(self.__movies).toarray()
        similarity=cosine_similarity(vector)
        
        distance=similarity[0]
        movielist=sorted(list(enumerate(distance)),reverse=True,key=(lambda x:x[1]))[0:10]
        movie_name=self.__movies[movielist[1][0]]
        
        del(self.__movies[0])
        
        return movie_name