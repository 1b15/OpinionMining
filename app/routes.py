import sys
from app import app
from flask import render_template, request, redirect, url_for, jsonify

from app.db_handler import get_user_profile, post_challenge, get_challenges, post_recipe, get_recipes, get_challenge, login

@app.route('/index')
@app.route('/', methods = ['GET'])
def weiter():
    return redirect(url_for('challengePage'))

@app.route('/challengePage', methods = ['GET'])
def challengePage():
    user_id = login(request.remote_addr)
    challengeList = get_challenges(user_id)
    return render_template('index.html', challengeList=challengeList)

@app.route('/recipePage/<challenge_id>', methods = ['GET'])
def recipe(challenge_id):
    user_id = login(request.remote_addr)
    challenge = get_challenge(user_id, int(challenge_id))
    recipeList = get_recipes(user_id, int(challenge_id))
    return render_template('challengeDetailsPage.html', challenge=challenge, recipeList=recipeList)

@app.route('/challenge', methods = ['POST'])
def challenge():
    if request.method == 'POST':
        req_data = request.data
        print(req_data)
    return render_template('index.html')

@app.route('/recipe/<challenge_id>', methods = ['POST'])
def add_recipe(challenge_id):
    if request.method == 'POST':
        user_id = login(request.remote_addr)
        req_data = request.get_json()
        post_recipe(req_data['text'], req_data['embed'], int(challenge_id), user_id)
        print(req_data)
    return jsonify(code='200')

@app.route('/vote', methods = ['GET'])
def vote():
    user_id = login(request.remote_addr)
    challengeList = get_challenges(user_id)
    return render_template('vote.html', challengeList=challengeList)
