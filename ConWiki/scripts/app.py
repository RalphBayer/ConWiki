from flask import Flask, render_template, request, make_response, jsonify, Markup
from article_manager import *
import os

cwd = os.getcwd().replace('\\','/')
app = Flask(__name__, template_folder=cwd + '/templates', static_folder=cwd + '/static')

address    = 'http://127.0.0.1:5000/'
iframe_src = {'sidebar': address + 'sidebar', 'topbar': address + 'topbar'}


# ----------------- Routes -----------------#
@app.route('/')
def index():
    return homepage()

@app.route('/homepage')
def homepage():
    return render_template('homepage.html', iframe_src=iframe_src)

@app.route('/about')
def about():
    return render_template('about.html', iframe_src=iframe_src)

@app.route('/create')
def create():
    return render_template('create.html', iframe_src=iframe_src)

@app.route('/help')
def help():
    return render_template('help.html', iframe_src=iframe_src)



@app.route('/sidebar')
def sidebar():
    return render_template('sidebar.html')

@app.route('/topbar')
def topbar():
    return render_template('topbar.html')



@app.route('/save_article', methods=['POST'])
def save_article():
    req = request.get_json()
    create_n_save_article(req)

    return make_response(jsonify({"message": "json received"}), 200)

@app.route('/load_article_html', methods=['POST', 'GET'])
def load_article_html():
    file_name = request.form.get('searchbar')
    html      = find_article(file_name)['data']['html']

    return render_template('article.html', name=file_name, gen_html=html, iframe_src=iframe_src)



if __name__ == '__main__':
    app.run()

# TODO:
#       CREATE FUNCTION TO SEND JSON DATA TO JAVASCRIPT
#       ADD MORE TOKENS TO THE Lexer CLASS.
