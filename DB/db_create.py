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
recipe['Text'] = ['', '']
recipe['Embed'] = ['', '']
recipe['Challenge'] = [0, 0, 1, 1]
recipe['Poster'] = [0, 1, 0, 1]

challengeLikes['User'] = [0, 1, 1]
challengeLikes['Challenge'] = [1, 0, 1]

recipeLikes['User'] = []
recipeLikes['Recipe'] = []