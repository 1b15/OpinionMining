import pandas as pd

users = {}
challenges = {}
recipe = {}
challengeLikes = {}
recipeLikes = {}

users['id'] = [0, 1]
users['Name'] = ['HansEntertainment', 'Jukamala']
users['Score'] = [0, 0]

challenges['id'] = [0, 1]
challenges['Title'] = ['Dessert mit Gurke', 'Schokokuchen mit wenig Kalorien']
challenges['Description'] = ['', 'Backe einen Schokoladenkuchen mit möglichst wenig Kalorien']
challenges['Difficulty'] = [4, 3]
categories = {'Backen': 0, 'Dessert': 1, 'Kochen': 2}
challenges['Category'] = [1, 0]
challenges['Poster'] = [0, 1]

recipe['id'] = [0, 1, 2, 3]
recipe['Text'] = ['Ich habe gerade eine tolle Torte gebacken, mit GURKEN!!!!',
                  'Plätzchen und das habe ich mit Gurken gemacht!\n \n Rezept:\n20 Gurken\nPlätzchenteig',
                  'Schau mal, ich habe die Challenges zerstört',
                  'Ich und meine Famillie haben das hier gezaubert als ich desletzt in den Anden wandern war'
                  ]
recipe['Embed'] = ['https://www.twitch.tv/namis_world/clip/SplendidBraveBarracudaOneHand',
                   'https://www.twitch.tv/kupferfuchs/clip/DepressedHotMilkTwitchRPG',
                   'https://imgur.com/r/Kochen/HdP1Pfl',
                   'https://imgur.com/r/Kochen/dsQ6xOn'
                   ]
recipe['Challenge'] = [0, 0, 1, 1]
recipe['Poster'] = [0, 1, 0, 1]

challengeLikes['User'] = [0, 1, 1]
challengeLikes['Challenge'] = [1, 0, 1]

recipeLikes['User'] = [0, 0]
recipeLikes['Recipe'] = [0, 1]

print(pd.DataFrame.from_dict(users))
print(pd.DataFrame.from_dict(challenges))
print(pd.DataFrame.from_dict(recipe))
print(pd.DataFrame.from_dict(challengeLikes))
print(pd.DataFrame.from_dict(recipeLikes))
pd.DataFrame.to_csv(pd.DataFrame.from_dict(users), './users.csv')
