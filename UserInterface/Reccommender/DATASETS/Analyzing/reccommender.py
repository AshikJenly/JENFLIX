import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class Reccomender():

    def __init__(self):
        self.__movie_data=pd.read_csv('Analyzed_DataSets/Final_movie.csv',index_col=0)
        self.__movie_data['tags']=self.__movie_data['tags'].apply(lambda x:eval(x))
        self.__movie_data['tags']=self.__movie_data['tags'].apply(lambda x:' '.join(x))

        print('Loaded all datas....')

        # COUNT VECTORIZER
        self.__cv=CountVectorizer(max_features=5000,stop_words='english')
        self.__vector=self.__cv.fit_transform(self.__movie_data['tags']).toarray() 
       

        print('count vectorization finished ....')

        #COSINE SIMILARITY
        self.__similarity=cosine_similarity(self.__vector)

        print('cosine smilarity calculated..')
    
    def getAppropriateMovieName(self,movie):
         self.__movie_name_cv=CountVectorizer(max_features=100,stop_words='english')
         self.movie_name_vector=self.__movie_name_cv.fit_transform(self.__movie_data['title']).toarray()
         pass
    def GetTopMovies(self,id):
            index=self.__movie_data[self.__movie_data['movie_id']==id].index[0]
            distance=self.__similarity[index]
            movielist=sorted(list(enumerate(distance)),reverse=True,key=(lambda x:x[1]))[0:10]
            
            movie_id_list=[]
            for i in movielist:
                # print(self.__movie_data.iloc[i[0]].title)
                movie_id_list.append(self.__movie_data.iloc[i[0]].movie_id)
            return movie_id_list
R1=Reccomender()
R1.GetTopMovies(19995)
