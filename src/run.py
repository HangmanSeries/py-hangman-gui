from canvas import Menu, Game
from tkinter import messagebox as msg
from pygame import mixer
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from player import Player

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client ()
mixer.init()

loses = 0
wins = 0

#firestore still unfinsihed
while(True):
    menu = Menu()
    game = Game()
    player = player = Player(menu.playername,0,0)
    if game.victory:
        mixer.music.load('Music/win.wav')
        player = Player(menu.playername,1,0)
    else:
        mixer.music.load('Music/lose.wav')
        player = Player(menu.playername,1,0)
    mixer.music.play()
    db.collection(u'scores').document(menu.playername).set(player.__dict__)

