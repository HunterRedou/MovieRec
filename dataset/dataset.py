import pandas as pd
import os
import opendatasets as od

#Assign the Url into a Variable
dataset = 'https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata'

#List all the Files
os.listdir("./tmdb-movie-metadata")

#List Content of the csv Files
movies = pd.read_csv("./tmdb-movie-metadata/tmdb_5000_movies.csv")

#Getting Series out of the Dataframe to categorise them
title = movies["title"]
genres = movies["genres"]
overview = movies["overview"]
popularity = movies["popularity"]
release_date = movies["release_date"]
runtime = movies["runtime"]
vote_average = movies["vote_average"]
vote_count = movies["vote_count"]
genres_no_na = movies[movies["genres"].notna()]

#iterate over Genres because its saved in a List (shown) but saved as a string, try to access the name of the Genres
for id, name in genres.items():
    print(f"name: {name}")
