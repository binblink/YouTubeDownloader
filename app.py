from pydub import AudioSegment
from tkinter.filedialog import askdirectory
from pytube import YouTube
from flask import Flask, render_template, request, flash
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'd24018a781de2dce4645ed646c6729328e9e71c0942a8eaa'

def getYTObjectWithItag(choice, yt):
    if choice=="mp4":
        return yt.streams.get_by_itag('22')
    else:
        return yt.streams.get_by_itag('251')
    
def getTitle(ytobject):
    return ytobject.streams[0].title

def getYTExtension(choice):
    if choice == "mp3":
        return "webm"
    else:
        return "mp4"

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
        ys = getYTObjectWithItag(choice, yt)
        title = getTitle(yt)
        yt_extension = getYTExtension(choice)
        
        # selection du dossier dans lequel enregistrer la vidéo
        path = askdirectory(title='Selectionnez un dossier pour enregistrer le fichier :')
        if choice == "mp3":
            ys.download()
            song = AudioSegment.from_file(title + "." + yt_extension, "webm")
            song.export(path+"/"+title + "."+choice, format="mp3")
            os.remove(title +"."+ yt_extension)
        else:
            ys.download(path)
         
    return render_template('ytdownload.html')