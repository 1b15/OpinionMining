import pandas as pd
import os

def generate_csv():
    users = {}
    challenges = {}
    recipes = {}
    challengeLikes = {}
    recipesLikes = {}

    users['id'] = [0, 1]
    users['Name'] = ['HansEntertainment', 'Jukamala']
    users['Score'] = [0, 0]
    users['Age'] = [20, 19]
    users['Gender'] = ['male', 'female']

    challenges['id'] = [0, 1]
    challenges['Title'] = ['Dessert mit Gurke', 'Schokokuchen mit wenig Kalorien']
    challenges['Description'] = ['', 'Backe einen Schokoladenkuchen mit möglichst wenig Kalorien']
    challenges['Difficulty'] = [4, 3]
    challenges['Category'] = [1, 0]
    challenges['Poster'] = [0, 1]

    recipes['id'] = [0, 1, 2, 3]
    recipes['Text'] = ['Ich habe gerade eine tolle Torte gebacken, mit GURKEN!!!!',
                      'Plätzchen und das habe ich mit Gurken gemacht!\n \n Rezept:\n20 Gurken\nPlätzchenteig',
                      'Schau mal, ich habe die Challenges zerstört',
                      'Ich und meine Famillie haben das hier gezaubert als ich desletzt in den Anden wandern war'
                      ]
    recipes['Embed'] = ['https://www.twitch.tv/namis_world/clip/SplendidBraveBarracudaOneHand',
                       'https://www.twitch.tv/kupferfuchs/clip/DepressedHotMilkTwitchRPG',
                       'https://imgur.com/r/Kochen/HdP1Pfl',
                       'https://imgur.com/r/Kochen/dsQ6xOn'
                       ]
    recipes['Challenge'] = [0, 0, 1, 1]
    recipes['Poster'] = [0, 1, 0, 1]

    challengeLikes['User'] = [0, 1, 1]
    challengeLikes['Challenge'] = [1, 0, 1]

    recipesLikes['User'] = [0, 0]
    recipesLikes['recipes'] = [0, 1]

    users_df = pd.DataFrame.from_dict(users)
    challenges_df = pd.DataFrame.from_dict(challenges)
    recipes_df = pd.DataFrame.from_dict(recipes)
    challengeLikes_df = pd.DataFrame.from_dict(challengeLikes)
    recipesLikes_df = pd.DataFrame.from_dict(recipesLikes)
    
    pd.DataFrame.to_csv(users_df, './users.csv', index=False)
    pd.DataFrame.to_csv(challenges_df, './challenges.csv', index=False)
    pd.DataFrame.to_csv(recipes_df, './recipes.csv', index=False)
    pd.DataFrame.to_csv(challengeLikes_df, './challengeLikes.csv', index=False)
    pd.DataFrame.to_csv(recipesLikes_df, './recipesLikes.csv', index=False)

if __name__ == '__main__':
    categories = {'Backen': 0, 'Dessert': 1, 'Kochen': 2}
    if not (os.path.exists('users.csv') and os.path.exists('recipesLikes.csv')):
        generate_csv()
    
