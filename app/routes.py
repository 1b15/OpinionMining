import sys
from app import app, APP_STATIC
from flask import render_template, request, redirect, url_for, jsonify
import os

from app.db_handler import get_user_profile, post_challenge, get_challenges, \
                           post_recipe, get_recipes, get_challenge, login, \
                           post_challengeLike, get_userRecipes, get_profile

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

@app.route('/challengeLike/<challenge_id>', methods = ['POST'])
def challengeLike(challenge_id):
    if request.method == 'POST':
        user_id = login(request.remote_addr)
        post_challengeLike(user_id, challenge_id)
    return jsonify(code='200')

@app.route('/recipe/<challenge_id>', methods = ['POST'])
def add_recipe(challenge_id):
    if request.method == 'POST':

        # Speichere Bild
        image = request.files["image"]
        image.save(os.path.join(app.root_path, 'static', 'img', image.filename))

        user_id = login(request.remote_addr)
        post_recipe(request.form['comment'], image.filename, int(challenge_id), user_id)

    return jsonify(code='200')

@app.route('/profile', methods = ['GET'])
def profile():
    user_id = login(request.remote_addr)
    profil = get_profile(user_id)
    recipeList = get_userRecipes(user_id)
    return render_template('profile.html', challenge=challenge, recipeList=recipeList)

@app.route('/vote', methods = ['GET'])
def vote():
    user_id = login(request.remote_addr)
    challengeList = get_challenges(user_id)
    return render_template('vote.html', challengeList=challengeList)
