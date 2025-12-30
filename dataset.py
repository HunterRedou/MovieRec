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

#Filter for Old Movies
def show_old():
    old_m = movies.sort_values(by="release_date")
    old = old_m.set_index("title")
    oldest_movies = old.release_date.head(5)
    print(oldest_movies)
    return old

#Filter for New Movies
def show_new():
    new_m = movies.sort_values(by="release_date", ascending=False)
    new = new_m.set_index("title")
    newest_movies = new.release_date.head(5)
    print(newest_movies)
    return new

# Get Desicrition of a Movie

def getting_description(user_input):
    new_ind = movies.set_index("title")
    pd.options.display.max_colwidth = 500
    print(
        new_ind.overview[user_input]
    )
    return new_ind.overview[user_input]

#Func to filter the Genre

def getting_genres(user_input):
    convert_str = str(user_input)
    found = False
    genre_list = []
    for i, value in movies["genres"].items():
        if convert_str in value:
            genre_list.append(i)
            found = True
    if not found:
        return ("This Genre does not exist. Please check if the first Letter of your Genre is a Upperletter. (Action, Sciene Fiction, Comedy)")
        
    
    genre_index_title = movies.loc[genre_list].set_index("title")
    print(
        genre_index_title.head(5)
    )
    return genre_index_title.head(5)

#Filter for the best rated Movies
def best_in_slot():
    best_m = movies.sort_values(by="vote_average", ascending=False)
    best = best_m.set_index("title")
    best_movies = best.vote_average.head(5)
    print(
        best_movies
    )
    return best_movies

#Filter for the length of a Movie
def runtime_movie(user_input):
    long = movies.set_index("title")
    long_movies = long.runtime[user_input]
    print(
        long_movies
    )
    return long_movies

