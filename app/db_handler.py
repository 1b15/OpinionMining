import pandas as pd

users = pd.read_csv('app/DB/users.csv', escapechar='\\').set_index('id')
challenges = pd.read_csv('app/DB/challenges.csv', escapechar='\\').set_index('id')
recipes = pd.read_csv('app/DB/recipes.csv', escapechar='\\').set_index('id')
challengeLikes = pd.read_csv('app/DB/challengeLikes.csv', escapechar='\\')
recipesLikes = pd.read_csv('app/DB/recipesLikes.csv', escapechar='\\')
loginData = pd.read_csv('app/DB/login.csv', escapechar='\\')

def login(user_ip):
    """
    Get saved user_id to ip or create new link
    """
    if user_ip in loginData['ip'].to_list():
        return loginData[loginData['ip'] == user_ip]['id'].item()
    else:
        user_id = loginData['id'].max() + 1
        loginData.loc[len(loginData)] = [user_id, user_ip]
        return user_id

def get_user_profile(user_id):
    user = users.iloc[user_id]
    return user['Name'], user['Score']

def get_challenge(user_id, challenge_id):
    """
    Get Info about specific challenge
    """
    chal = challenges.iloc[challenge_id].to_dict()
    chal['id'] = challenge_id
    chal['Poster'] = users.iloc[chal['Poster']]['Name']
    chal['Likes'] = len(challengeLikes[challengeLikes['Challenge'] == challenge_id])
    chal['Liked'] = 0
    if challenge_id in challengeLikes[challengeLikes['User'] == user_id].values:
        chal['Liked'] = 1
    return chal

def get_challenges(user_id):
    """
    Sortiert nach Likes:
    Gebe die 10 Einträge der Seite pageNumber zurückgegeben.
    (pageNumber * 10 bis [pageNumber+1] * 10 - 1)
    """
    #Anzahl Beiträge
    counter = pd.DataFrame({'id':challenges.index.values, 'Count':[0]*len(challenges.index.values)}).set_index('id')
    countIds = recipes.groupby('Challenge').count()
    counter.at[countIds.index.values, 'Count'] = countIds['Text']

    #Persönlicher Like
    liked = pd.DataFrame({'id': challenges.index.values, 'Liked': [0] * len(challenges.index.values)}).set_index('id')
    LikeIds = challengeLikes[challengeLikes['User'] == user_id]['Challenge'].astype(int)
    liked.at[LikeIds, 'Liked'] = 1

    #Likes
    challengeLikes['Challenge'] = challengeLikes['Challenge'].astype(int)
    sortedIds = challengeLikes.groupby('Challenge').count().sort_values(by='User', ascending=False)

    #Challenges mit 0 Likes
    missingChallenges = challenges[~challenges.index.isin(sortedIds.index.values)]
    missingIds = pd.DataFrame({'id': missingChallenges.index.values, 'User': [0] * len(missingChallenges)}).set_index('id')
    sortedIds = pd.concat([sortedIds, missingIds])#.iloc[pageNumber * 10:(pageNumber + 1) * 10]

    challengelist = challenges.iloc[sortedIds.index.values]
    challengelist['Likes'] = sortedIds['User'].copy().astype(int)
    challengelist['Poster'] = [users.iloc[x]['Name'] for x in challengelist['Poster']]
    challengelist['Counter'] = counter['Count']
    challengelist['Liked'] = liked['Liked'].copy().astype(int)

    print(challengelist)
    dict = challengelist.to_dict('index')
    return [{**x, 'id':x1} for (x1,x) in zip(dict.keys(), dict.values())]

def get_recipes(user_id, challenge_id):
    """
    Sortiert nach Likes:
    Gebe die 10 Einträge der Seite pageNumber zurückgegeben.
    (pageNumber * 10 bis [pageNumber+1] * 10 - 1)
    """
    #Relevanten Daten betrachten
    relevantRecipes = recipes[recipes['Challenge'] == challenge_id]
    relevantLikes = recipesLikes[recipesLikes['recipes'].isin(relevantRecipes.index.values)]
    sortedIds = relevantLikes.groupby('recipes').count().sort_values(by='User', ascending=False)

    # Persönlicher Like
    liked = pd.DataFrame({'id':relevantRecipes.index.values, 'Liked': [0] * len(relevantRecipes.index.values)}).set_index('id')
    LikeIds = relevantLikes[relevantLikes['User'] == user_id]['recipes']
    liked.at[LikeIds, 'Liked'] = 1

    #Recipes mit 0 Likes
    missingRecipes = relevantRecipes[~relevantRecipes.index.isin(relevantLikes['recipes'])]
    missingIds = pd.DataFrame({'id':missingRecipes.index.values, 'User':[0] * len(missingRecipes)}).set_index('id')
    sortedIds = pd.concat([sortedIds, missingIds])#.iloc[pageNumber * 10:(pageNumber + 1) * 10]

    recipelist = recipes.iloc[sortedIds.index.values]
    recipelist['Likes'] = sortedIds['User'].copy().astype(int)
    recipelist['Poster'] = [users.iloc[x]['Name'] for x in recipelist['Poster']]
    recipelist['Liked'] = liked['Liked'].copy().astype(int)

    print(recipelist)
    dict = recipelist.to_dict('index')
    return [{**x, 'id': x1} for (x1, x) in zip(dict.keys(), dict.values())]

def get_userRecipes(user_id):
    relevantRecipes = recipes[recipes['Poster'] == user_id]
    relevantLikes = recipesLikes[recipesLikes['recipes'].isin(relevantRecipes.index.values)]
    sortedIds = relevantLikes.groupby('recipes').count().sort_values(by='User', ascending=False)

    liked = pd.DataFrame({'id':relevantRecipes.index.values, 'Liked': [0] * len(relevantRecipes.index.values)}).set_index('id')
    LikeIds = relevantLikes[relevantLikes['User'] == user_id]['recipes']
    liked.at[LikeIds, 'Liked'] = 1

    missingRecipes = relevantRecipes[~relevantRecipes.index.isin(relevantLikes['recipes'])]
    missingIds = pd.DataFrame({'id':missingRecipes.index.values, 'User':[0] * len(missingRecipes)}).set_index('id')
    sortedIds = pd.concat([sortedIds, missingIds])

    recipelist = recipes.iloc[sortedIds.index.values]
    recipelist['Likes'] = sortedIds['User'].copy().astype(int)
    recipelist['Poster'] = [users.iloc[x]['Name'] for x in recipelist['Poster']]
    recipelist['Liked'] = liked['Liked'].copy().astype(int)

    print(recipelist)
    dict = recipelist.to_dict('index')
    return [{**x, 'id': x1} for (x1, x) in zip(dict.keys(), dict.values())]   


def post_challenge(title, description, difficulty, category, poster_id):
    challenges.loc[len(challenges)] = [title, description, difficulty, category, poster_id]
    return True

def post_recipe(text, embed, challenge_id, poster_id):
    recipes.loc[len(recipes)] = [text, embed, challenge_id, poster_id]
    return True

def post_challengeLike(user_id, challenge_id):
    like = challengeLikes[(challengeLikes['Challenge'] == challenge_id)
                          & (challengeLikes['User'] == user_id)]
    if like.empty:
        challengeLikes.loc[challengeLikes.index.values[-1]+1] = [user_id, challenge_id]
        users.at[user_id, 'Score'] += 1
    else:
        challengeLikes.drop(like.index.values, inplace=True)
        users.at[user_id, 'Score'] -= 1
    return True

def post_recipeLike(user_id, recipe_id):
    like = recipesLikes[(recipesLikes['recipes'] == recipe_id)
                          & (recipesLikes['User'] == user_id)]
    if like.empty:
        recipesLikes.loc[recipesLikes.index.values[-1]+1] = [user_id, recipe_id]
        users.at[user_id, 'Score'] += 1
    else:
        recipesLikes.drop(like.index.values, inplace=True)
        users.at[user_id, 'Score'] -= 1
    return True

def get_profile(user_id):
    userdict = users.iloc[user_id].to_dict()
    return userdict

if __name__ == '__main__':
    #print(get_recipes(0, 46))
    #print(get_challenge(0, 46))
    #print(get_challenges(0))
    import pdb; pdb.set_trace()