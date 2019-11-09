from flask import Flask
import pandas as pd

users = pd.read_csv('DB/users.csv').set_index('id')
challenges = pd.read_csv('DB/challenges.csv').set_index('id')
recipes = pd.read_csv('DB/recipes.csv').set_index('id')
challengeLikes = pd.read_csv('DB/challengeLikes.csv')
recipesLikes = pd.read_csv('DB/recipesLikes.csv')

app = Flask(__name__)

from app import routes
