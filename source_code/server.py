import re
from flask import Flask, flash, render_template, redirect, url_for, request, session, Response
from flask_wtf.csrf import CSRFProtect
from flask_cors import CORS, cross_origin
from module.database import Database
import os

app = Flask(__name__)
app.config['WTF_CSRF_ENABLED'] = True
csrf = CSRFProtect()
csrf.init_app(app)
CORS(app, resources={r"/*": {"origins": "*", "send_wildcard": "False"}})
app._static_folder = "static"
app.secret_key = os.getenv('API_SECRET_KEY')
db = Database()
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
@cross_origin()
def index():
    data = db.read(None)

    return Response(render_template('index.html', data = data), 200)

@app.route('/add/')
def add():
    return Response(render_template('add.html'), 200)

@app.route('/addphone', methods = ['POST', 'GET'])
def addphone():
    if request.method == 'POST' and request.form['save']:
        if db.insert(request.form):
            flash("A new phone number has been added")
        else:
            flash("A new phone number can not be added")

        return Response(url_for('index'), 301)
    else:
        return Response(url_for('index'), 301)

@app.route('/update/<int:id>/')
def update(id):
    data = db.read(id);

    if len(data) == 0:
        return redirect(url_for('index'))
    else:
        session['update'] = id
        return Response(render_template('update.html', data = data), 200)

@app.route('/updatephone', methods = ['POST'])
def updatephone():
    if request.method == 'POST' and request.form['update']:

        if db.update(session['update'], request.form):
            flash('A phone number has been updated')

        else:
            flash('A phone number can not be updated')

        session.pop('update', None)

        return Response(url_for('index'), 301)
    else:
        return Response(url_for('index'), 301)

@app.route('/delete/<int:id>/')
def delete(id):
    data = db.read(id);

    if len(data) == 0:
        return Response(url_for('index'), 200)
    else:
        session['delete'] = id
        return Response(render_template('delete.html', data = data), 200)

@app.route('/deletephone', methods = ['POST'])
def deletephone():
    if request.method == 'POST' and request.form['delete']:

        if db.delete(session['delete']):
            flash('A phone number has been deleted')

        else:
            flash('A phone number can not be deleted')

        session.pop('delete', None)

        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.route('/static/css')
def send_css(path):
    return send_from_directory('static/css', path,mimetype='text/css')

@app.errorhandler(404)
def page_not_found(error):
    return Response(render_template('error.html'), 200)

if __name__ == '__main__':
    app.run(port=5000, host="0.0.0.0")
