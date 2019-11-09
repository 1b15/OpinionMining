import pandas as pd

users = pd.read_csv('app/DB/users.csv').set_index('id')
challenges = pd.read_csv('app/DB/challenges.csv').set_index('id')
recipes = pd.read_csv('app/DB/recipes.csv').set_index('id')
challengeLikes = pd.read_csv('app/DB/challengeLikes.csv')
recipesLikes = pd.read_csv('app/DB/recipesLikes.csv')

def get_user_profile(user_id):
    user = users.iloc[user_id]
    return user['Name'], user['Score']

def get_challenge(challenge_id):
    """
    Get Info about specific challenge
    """
    chal = challenges.iloc[challenge_id].to_dict()
    chal['Likes'] = len(challengeLikes[challengeLikes['Challenge'] == challenge_id])
    return chal

def get_challenges():
    """
    Sortiert nach Likes:
    Gebe die 10 Einträge der Seite pageNumber zurückgegeben.
    (pageNumber * 10 bis [pageNumber+1] * 10 - 1)
    """
    counter = pd.DataFrame({'id':challenges.index.values, 'Count':[0]*len(challenges.index.values)}).set_index('id')
    countIds = recipes.groupby('Challenge').count()
    counter.at[countIds.index.values, 'Count'] = countIds['Text']

    sortedIds = challengeLikes.groupby('Challenge').count().sort_values(by='User', ascending=False)

    #Challenges mit 0 Likes
    missingChallenges = challenges[~challenges.index.isin(challengeLikes.index.values)]
    missingIds = pd.DataFrame({'id': missingChallenges.index.values, 'User': [0] * len(missingChallenges)}).set_index('id')
    sortedIds = pd.concat([sortedIds, missingIds])#.iloc[pageNumber * 10:(pageNumber + 1) * 10]

    challengelist = challenges.iloc[sortedIds.index.values]
    challengelist['Likes'] = sortedIds['User'].copy().astype(int)
    challengelist['Poster'] = [users.iloc[x]['Name'] for x in challengelist['Poster']]
    challengelist['Counter'] = counter['Count']

    dict = challengelist.to_dict('index')
    return [{**x, 'id':x1} for (x1,x) in zip(dict.keys(), dict.values())]

def get_recipes(challenge_id):
    """
    Sortiert nach Likes:
    Gebe die 10 Einträge der Seite pageNumber zurückgegeben.
    (pageNumber * 10 bis [pageNumber+1] * 10 - 1)
    """
    #Relevanten Daten betrachten
    relevantRecipes = recipes[recipes['Challenge'] == challenge_id]
    relevantLikes = recipesLikes[recipesLikes['recipes'].isin(relevantRecipes.index.values)]
    sortedIds = relevantLikes.groupby('recipes').count().sort_values(by='User', ascending=False)

    #Recipes mit 0 Likes
    missingRecipes = relevantRecipes[~relevantRecipes.index.isin(relevantLikes.index.values)]
    missingIds = pd.DataFrame({'id':missingRecipes.index.values, 'User':[0] * len(missingRecipes)}).set_index('id')
    sortedIds = pd.concat([sortedIds, missingIds])#.iloc[pageNumber * 10:(pageNumber + 1) * 10]

    recipelist = recipes.iloc[sortedIds.index.values]
    recipelist['Likes'] = sortedIds['User'].copy().astype(int)
    recipelist['Poster'] = [users.iloc[x]['Name'] for x in recipelist['Poster']]
    print(recipelist)
    dict = recipelist.to_dict('index')
    return [{**x, 'id': x1} for (x1, x) in zip(dict.keys(), dict.values())]

def post_challenge(title, description, difficulty, category, poster):
    challenges.loc[len(challenges)] = [title, description, difficulty, category, poster]
    return True

def post_challengeLike(user_id, challenge_id):
    challengeLikes.loc[len(challengeLikes)] = [user_id, challenge_id]
    user.iloc[user_id].Score += 1
    return True

if __name__ == '__main__':
    #print(get_recipes(0))
    #print(get_challenge(46))
    print(get_challenges())