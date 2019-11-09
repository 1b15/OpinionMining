import pandas as pd

users = pd.read_csv('app/DB/users.csv').set_index('id')
challenges = pd.read_csv('app/DB/challenges.csv').set_index('id')
recipes = pd.read_csv('app/DB/recipes.csv').set_index('id')
challengeLikes = pd.read_csv('app/DB/challengeLikes.csv')
recipesLikes = pd.read_csv('app/DB/recipesLikes.csv')

def get_user_profile(user_id):
    user = users.iloc[user_id]
    return user['Name'], user['Score']

def get_challenges(pageNumber):
    """
    Sortiert nach Likes:
    Gebe die 10 Einträge der Seite pageNumber zurückgegeben.
    (pageNumber * 10 bis [pageNumber+1] * 10)
    """
    sortedIds = challengeLikes.groupby('Challenge').count().sort_values(by='User', ascending=False).iloc[pageNumber*10:(pageNumber+1)*10]
    challengelist = challenges.iloc[sortedIds.index.values]
    challengelist['Likes'] = sortedIds['User']
    challengelist['Poster'] = users.iloc[challengelist['Poster']]['Name']
    print(challengelist)
    return list(challengelist.to_dict('index').values())

def post_challenge(title, description, difficulty, category, poster):
    challenges.loc[len(challenges)] = [title, description, difficulty, category, poster]
    return True

if __name__ == '__main__':
    print(get_challenges(0))