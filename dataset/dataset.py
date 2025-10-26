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

