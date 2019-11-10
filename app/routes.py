import sys
from app import app, APP_STATIC
from flask import render_template, request, redirect, url_for, jsonify
import os

from app.db_handler import get_user_profile, post_challenge, get_challenges, get_recipes, get_challenge, login

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

        image = request.files["image"] #image.fileename ->Name des Bildes
        print(request.form['comment']) #Freitext

        image.save(os.path.join(app.root_path, 'static', 'img', image.filename)) #Speichere Bild ab

    return jsonify(code='200')

@app.route('/vote', methods = ['GET'])
def vote():
    return render_template('vote.html')

@app.route("/uploadImage", methods=["POST"])
def upload_image():
    if request.files:
        image = request.files["image"]
        print(request.form['comment'])
        image.save(os.path.join(app.root_path, 'static', 'img', image.filename))

        print("Image saved")

        return redirect('/')
    return redirect(request.url)
