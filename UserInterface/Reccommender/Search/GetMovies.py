
import pandas as pd


MOVIE_DATA=pd.read_csv('static/DATASETS/movies.csv')
MOVIE_DATA['index']=MOVIE_DATA['id']
MOVIE_DATA=MOVIE_DATA.set_index('index')

class AMovie():
    def __init__(self,id):
        try:
            # MOVIE_DATA=None
            # id=19995
            df=MOVIE_DATA[MOVIE_DATA['id']==id]
            
           
        except Exception as e:
            print('Wrong id',e)
        try:
            self.name=df.loc[id,'title']
           
            self.link=df.loc[id,'homepage']
           
            self.releaseDate=df.loc[id,'release_date']
            self.runtime=df.loc[id,'runtime']
            self.tagline=df.loc[id,'tagline']
            self.vote=df.loc[id,'vote_average']
        except:
            
            print('error')
            
class GetFirst():
    def __init__(self):
        df=pd.read_csv('static/DATASETS/movies.csv',index_col=0)
        df.reset_index(inplace=True)
        df=df[df['vote_count']>=1000]
        vc_list=df.sort_values(by='vote_count',ascending=False)[0:18]
        self.__top_f=df.sort_values(by='vote_average',ascending=False)[0:15]
    def getTop15Ids(self):
        ids=[]
        for i in self.__top_f['id']:
            ids.append(i)
        return ids
        
class GetMovies():

    """Gets list of movie ids and return list of movie objects"""
    # def getMovie(self):

    #     m1={'name':'Avatar','Actor':'simeone','director':'james'}
    #     m2={'name':'SUperman','Actor':'simeone','director':'james'}
    #     m3={'name':'ironman','Actor':'simeone','director':'james'}
    #     m4={'name':'Thor','Actor':'simeone','director':'james'}
    #     m5={'name':'Love today','Actor':'simeone','director':'james'}

    #     context=[m1,m2,m3,m4,m5]

    #     return context
    def getMovieObjs(self,movie_ids):
        movie_obj_list=[]
        mv=None
        for id in movie_ids:
            mv=AMovie(id=id)
            movie_obj_list.append(mv)

        return movie_obj_list
        

