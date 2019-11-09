from app import app
from flask import render_template, request

from app.db_handler import get_user_profile, post_challenge, get_challenges, get_recipes, get_challenge

@app.route('/')
@app.route('/index', methods = ['GET'])
def index():
    challengeList = get_challenges()
    return render_template('index.html', challengeList=challengeList)

@app.route('/challengePage', methods = ['GET'])
def challengePage():
    challengeList = get_challenges()
    return render_template('index.html', challengeList=challengeList)

@app.route('/recipePage/<challenge_id>', methods = ['GET'])
def recipe(challenge_id):
    challenge = get_challenge(int(challenge_id))
    recipeList = get_recipes(int(challenge_id))
    return render_template('challengeDetailsPage.html', challenge=challenge, recipeList=recipeList)

@app.route('/challenge', methods = ['POST','GET'])
def challenge():
    if request.method == 'POST':
        req_data = request.data
        print(req_data)
    return render_template('index.html')

@app.route('/challengeDetailsPage', methods = ['GET'])
def challengeDetailsPage():
    return render_template('challengeDetailsPage.html')

