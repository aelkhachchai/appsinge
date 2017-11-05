#!/usr/bin/env python3

from flask import Flask, url_for, render_template

app = Flask(__name__)

app.debug = True
app.secret_key = '&7dl-gxw_q=wksvia$d4rrs!e_@9hyf*oy41#j*ed8%wzgap6q'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/singeries')
def singe():
    return render_template('singeries.html')

@app.route('/singeries/alidodo')
def alidodo():
    alidodo = [f'{i}ali.jpg' for i in range(1, 13)]
    return render_template('alidodo.html', alidodo=alidodo)

@app.route('/trombinoscope')
def trombi():
    appsinges = [
        {'uid': 0, 'log': 'achraf.el-khachchai', 'img': 'goteki.jpg'},
        {'uid': 1, 'log': 'nathan.quintard', 'img': 'oignon.jpg'}
    ]
    return render_template('trombi.html', appsinges=appsinges)

@app.route('/trombinoscope/<int:uid>')
def show(uid: int):
    appsinge = {
        'login': 'achraf.el-khachchai',
        'pseudo': 'Goteki',
        'firstname': 'Achraf',
        'lastname': 'El Khachchai',
        'email': 'el.achraf150@gmail.com',
        'img': 'goteki.jpg',
        'birthdate': '29/10/1995'
    }
    return render_template('show.html', user=appsinge)

@app.route('/condingstyle')
def code():
    return render_template('code.html')

@app.route('/condingstyle/roi')
def king():
    return render_template('king.html')

@app.route('/condingstyle/héro')
def hero():
    return render_template('hero.html')

@app.route('/condingstyle/hymne')
def song():
    return render_template('song.html')

@app.route('/condingstyle/symbole')
def symbol():
    return render_template('symbol.html')

@app.route('/condingstyle/jeu')
def game():
    return render_template('game.html')

if __name__ == '__main__':
    app.run()
