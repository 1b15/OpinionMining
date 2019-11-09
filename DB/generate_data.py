import itertools
import random

import numpy as np
import pandas as pd


def generate_csv():
    users = {}
    challenges = {}
    recipes = {}
    challenge_likes = {}
    recipes_likes = {}

    # ---------- USER DATA ----------

    ages = [random.randint(17, 60) for _ in range(200)]
    genders = ['male'] * 100 + ['female'] * 100

    df = pd.read_csv('twitter_usernames.csv')
    names = list(itertools.chain(*df.sample(n=200).values.tolist()))
    scores = [random.randint(0, 45) for _ in range(200)]
    ids = np.arange(0, 200)

    users['id'] = ids
    users['Name'] = names
    users['Score'] = scores
    users['Age'] = ages
    users['Gender'] = genders

    # ---------- CHALLENGE DATA ----------

    challenge_ids = np.arange(0, 120)
    challenge_titles = ['title...'] * 120  # TODO
    challenge_desc = ['...'] * 120  # TODO
    challenge_diff = [random.randint(1, 3) for _ in range(60)] + [random.randint(4, 5) for _ in range(60)]
    challenge_cats = [0] * 40 + [1] * 40 + [2] * 40
    challenge_posters = np.random.choice(ids, 120)

    challenges['id'] = challenge_ids
    challenges['Title'] = challenge_titles
    challenges['Description'] = challenge_desc
    challenges['Difficulty'] = challenge_diff
    challenges['Category'] = challenge_cats
    challenges['Poster'] = challenge_posters

    # ---------- RECIPE DATA ----------

    # df = pd.read_csv('twitter_comments.csv')
    # comments = list(itertools.chain(*df.sample(n=100).values.tolist()))

    with open('rezepte_deutsch', 'r') as file:
        data = file.read()
        new_recipes = data.split('Rezept:')
        new_recipes = [recipe.replace('\n', ' ') for recipe in new_recipes]

    recipes['id'] = np.arange(100)
    recipes['Text'] = np.random.choice(new_recipes, 100)
    recipes['Embed'] = np.zeros(100)
    # recipes['Embed'] = ['https://www.twitch.tv/namis_world/clip/SplendidBraveBarracudaOneHand',
    #                     'https://www.twitch.tv/kupferfuchs/clip/DepressedHotMilkTwitchRPG',
    #                     'https://imgur.com/r/Kochen/HdP1Pfl',
    #                     'https://imgur.com/r/Kochen/dsQ6xOn'
    #                     ]
    recipes['Challenge'] = np.random.choice(challenge_ids, 100)
    recipes['Poster'] = np.random.choice(ids, 100)

    # ---------- GENERATE TEST DATA FOR LIKES ----------

    likes = []
    likes_ids = []

    for id in ids:
        found = False
        while not found:
            random_recipe = random.randint(0, 99)
            if recipes['Poster'][random_recipe] is not id:
                likes.append(random_recipe)
                likes_ids.append(id)
                found = True
        found = False
        r = random.uniform(0, 1)
        while r > 0.5:
            while not found:
                random_recipe = random.randint(0, 99)
                if recipes['Poster'][random_recipe] is not id:
                    likes.append(random_recipe)
                    likes_ids.append(id)
                    found = True
            found = False
            r = random.uniform(0, 1)

    recipes_likes['User'] = likes_ids
    recipes_likes['recipes'] = likes

    liking_users = []
    liked_challenges = []

    male = ids[:100]
    female = ids[100:]

    for id in male:
        if ages[id] < 28:
            r = random.randint(5, 15)
            x = [id] * r
            liking_users.extend(x)
            y = np.random.choice(challenge_ids[80:120], r)
            liked_challenges.extend(y)

            r = random.randint(1, 15)
            x = [id] * r
            liking_users.extend(x)
            y = np.random.choice(challenge_ids[40:80], r)
            liked_challenges.extend(y)

            r = random.randint(1, 5)
            x = [id] * r
            liking_users.extend(x)
            y = np.random.choice(challenge_ids[:40], r)
            liked_challenges.extend(y)
    for id in male:
        if ages[id] >= 28:
            r = random.randint(1, 7)
            x = [id] * r
            liking_users.extend(x)
            y = np.random.choice(challenge_ids[80:120], r)
            liked_challenges.extend(y)

            r = random.randint(1, 10)
            x = [id] * r
            liking_users.extend(x)
            y = np.random.choice(challenge_ids[40:80], r)
            liked_challenges.extend(y)

            r = random.randint(1, 8)
            x = [id] * r
            liking_users.extend(x)
            y = np.random.choice(challenge_ids[:40], r)
            liked_challenges.extend(y)

    for id in female:
        if ages[id] < 28:
            r = random.randint(1, 8)
            x = [id] * r
            liking_users.extend(x)
            y = np.random.choice(challenge_ids[80:120], r)
            liked_challenges.extend(y)

            r = random.randint(5, 15)
            x = [id] * r
            liking_users.extend(x)
            y = np.random.choice(challenge_ids[40:80], r)
            liked_challenges.extend(y)

            r = random.randint(1, 15)
            x = [id] * r
            liking_users.extend(x)
            y = np.random.choice(challenge_ids[:40], r)
            liked_challenges.extend(y)
    for id in female:
        if ages[id] >= 28:
            r = random.randint(1, 7)
            x = [id] * r
            liking_users.extend(x)
            y = np.random.choice(challenge_ids[80:120], r)
            liked_challenges.extend(y)

            r = random.randint(1, 5)
            x = [id] * r
            liking_users.extend(x)
            y = np.random.choice(challenge_ids[40:80], r)
            liked_challenges.extend(y)

            r = random.randint(1, 10)
            x = [id] * r
            liking_users.extend(x)
            y = np.random.choice(challenge_ids[:40], r)
            liked_challenges.extend(y)

    challenge_likes['User'] = liking_users
    challenge_likes['Challenge'] = liked_challenges

    # Save data

    users_df = pd.DataFrame.from_dict(users)
    challenges_df = pd.DataFrame.from_dict(challenges)
    recipes_df = pd.DataFrame.from_dict(recipes)
    challengeLikes_df = pd.DataFrame.from_dict(challenge_likes)
    recipesLikes_df = pd.DataFrame.from_dict(recipes_likes)

    pd.DataFrame.to_csv(users_df, './users.csv', index=False)
    pd.DataFrame.to_csv(challenges_df, './challenges.csv', index=False)
    pd.DataFrame.to_csv(recipes_df, './recipes.csv', index=False)
    pd.DataFrame.to_csv(challengeLikes_df, './challengeLikes.csv', index=False)
    pd.DataFrame.to_csv(recipesLikes_df, './recipesLikes.csv', index=False)


if __name__ == '__main__':
    categories = {'Backen': 0, 'Dessert': 1, 'Kochen': 2}
    generate_csv()
    # if not (os.path.exists('users.csv') and os.path.exists('recipesLikes.csv')):
    #   generate_csv()
