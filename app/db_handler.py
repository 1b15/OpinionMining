import pandas as pd

users = pd.read_csv('DB/users.csv').set_index('id')
challenges = pd.read_csv('DB/challenges.csv').set_index('id')
recipes = pd.read_csv('DB/recipes.csv').set_index('id')
challengeLikes = pd.read_csv('DB/challengeLikes.csv')
recipesLikes = pd.read_csv('DB/recipesLikes.csv')

def get_user_profile(user_id):
    user = users.iloc[user_id]
    return user['Name'], user['Score']


def post_challenge(title, description, difficulty, category, poster):
    challenges.loc[len(challenges)] = [title, description, difficulty, category, poster]
    return True