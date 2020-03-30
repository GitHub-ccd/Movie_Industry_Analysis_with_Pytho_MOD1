#importing libraries
import pandas as pd 
import numpy as np

# Load files to dataframes
# IMDB 
name=pd.read_csv('Data/imdb.name.basics.csv')
takas=pd.read_csv('Data/imdb.title.akas.csv')
tbasics=pd.read_csv('Data/imdb.title.basics.csv')
crew=pd.read_csv('Data/imdb.title.crew.csv')
principals=pd.read_csv('Data/imdb.title.principals.csv')
ratings=pd.read_csv('Data/imdb.title.ratings.csv')
# Box Office Mojo 
bom=pd.read_csv('Data/bom.movie_gross.csv')
# Rotten Tomatoes
rt=pd.read_csv('Data/rt.movie_info.tsv', sep='\t')
rt_reviews=pd.read_csv('Data/rt.reviews.tsv', delimiter='\t', encoding='latin-1') # encoding worked!!! with correct delimiter 
# TheMovieDB.org
tmdb=pd.read_csv('Data/tmdb.movies.csv')
# no idea where this is from 
tn_budgets=pd.read_csv('Data/tn.movie_budgets.csv')
# list of df[name ,takas ,tbasics ,crew ,principals ,ratings ,bom ,rt ,rt_reviews ,tmdb ,tn_budgets]

dflist=[name ,takas ,tbasics ,crew ,principals ,ratings ,bom ,rt ,rt_reviews ,tmdb ,tn_budgets]

bom.info()
bom.head(3)

bom.title.astype()