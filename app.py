from tkinter import Tk
from tkinter.filedialog import askdirectory
from pytube import YouTube
from flask import Flask, render_template, request, url_for, flash, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'd24018a781de2dce4645ed646c6729328e9e71c0942a8eaa'

def getFormat(choice, yt, format):
    if choice==format:
        return yt.streams.get_by_itag('22')
    else:
        return yt.streams.get_by_itag('251')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download/', methods=('GET', 'POST'))
def download():
    link = request.form['yt_link']
    choice = request.form['option']
    if not link:
            flash('Veuillez entrer un lien pour continuer.')
    
    elif request.method == 'POST':
        # recuperation de l'input du formulaire
        link = request.form['yt_link']
        choice = request.form['option']
        yt = YouTube(link)
        ys = getFormat(choice, yt, choice)
        # selection du dossier dans lequel enregistrer la vidéo
        path = askdirectory(title='Selectionnez un dossier pour enregistrer la video :')
        ys.download(path)
         
    return render_template('ytdownload.html')

