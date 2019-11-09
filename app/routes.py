from app import app
from flask import render_template
from flask import request

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/challenge', methods=["POST"])
def challenge():
    print(request.is_json)
    content = request.get_json()
    print(content)
    return "Hallo"