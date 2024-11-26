import time
import json
import random
import pygame
import tkinter as tk
from tkinter import messagebox

pygame.mixer.init()

with open("songs.json", "r") as f:
    songs = json.load(f)

random.shuffle(songs)

songs = [
    {"file": "song3.mp3", "title": "Last Christmas"},
    {"file": "song3.mp3", "title": "Jingle Bells"},
    {"file": "song3.mp3", "title": "It's Beginning to Look a Lot Like Christmas"},
    {"file": "song3.mp3", "title": "Jingle Bell Rock"},
    {"file": "song3.mp3", "title": "All I Want for Christmas is You"},
    {"file": "song3.mp3", "title": "Let it Snow!"},            
       ]

def play_song_clip():
    pygame.mixer.music.play()
    start_time = time.time()
    while pygame.mixer.music.get_busy(): 
        if time.time() - start_time > 5:
            pygame.mixer.music.stop()
            break
        time.sleep(0.5)
    pygame.mixer.music.stop()

def show_song_clip():
    song = songs[0]  
    play_song_clip()

root = tk.Tk()
root.title("Christmas Song Player")

play_button = tk.Button(root, text="Play Song Clip", command=show_song_clip)
play_button.pack(pady=20)

root.mainloop()
