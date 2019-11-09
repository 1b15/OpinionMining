from app import app
from flask import render_template, request

from app.db_handler import get_user_profile, post_challenge, get_challenges

@app.route('/')
@app.route('/index', methods = ['POST','GET'])
def index():
    challengeList = get_challenges(0)
    return render_template('index.html', challengeList=challengeList)

@app.route('/challengePage/<pageNumber>', methods = ['GET'])
def challengePage(pageNumber):
    challengeList = get_challenges(int(pageNumber))
    return render_template('challengeList.html', challengeList=challengeList)

@app.route('/challenge', methods = ['POST','GET'])
def challenge():
    if request.method == 'POST':
        req_data = request.data
        print(req_data)
        #test_text(**req_data)
    return render_template('index.html')

