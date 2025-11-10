import pandas as pd
import os
import json
import opendatasets as od
import sys


#Assign the Url into a Variable
dataset = 'https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata'

#List all the Files
os.listdir("/home/philipp/Projects/MovieRec/dataset/tmdb-movie-metadata")

#List Content of the csv Files
movies = pd.read_csv("/home/philipp/Projects/MovieRec/dataset/tmdb-movie-metadata/tmdb_5000_movies.csv")

old_m = movies.sort_values(by="release_date")
old = old_m.set_index("title")
oldest_movies = old.release_date.head(5)



new_m = movies.sort_values(by="release_date", ascending=False)
new = new_m.set_index("title")
newest_movies = new.release_date.head(5)


print(type(movies))
print(type(movies.genres))
mo = movies.genres
i = input()
inp = str(i)
for i, value in mo.items():
    if inp in value:
        print(f'Index: {i} Value: {value}')

#f r genre in movies.genres:
#    print(type(genre))
