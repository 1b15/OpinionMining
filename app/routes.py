from app import app
from flask import render_template, request

from app.db_handler import get_user_profile, post_challenge, get_challenges, get_recipes, get_challenge, login

@app.route('/')
@app.route('/index', methods = ['GET'])
def index():
    challengeList = get_challenges()
    return render_template('index.html', challengeList=challengeList)

@app.route('/challengePage', methods = ['GET'])
def challengePage():
    user_id = login(request.remote_addr)
    print(user_id)
    challengeList = get_challenges(user_id)
    return render_template('index.html', challengeList=challengeList)

@app.route('/recipePage/<challenge_id>', methods = ['GET'])
def recipe(challenge_id):
    user_id = login(request.remote_addr)
    challenge = get_challenge(user_id, int(challenge_id))
    recipeList = get_recipes(user_id, int(challenge_id))
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

