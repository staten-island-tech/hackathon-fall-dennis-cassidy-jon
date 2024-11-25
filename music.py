import time
import json
import random
import pygame 
import tkinter as tk
from tkinter import messagebox


with open ("songs.json", "r") as f:
    songs = json.load (f)
    
random.shuffle(songs)

songs = [
    {"file": "song1.mp3", "title": "Last Christmas"},
    {"file": "song2.mp3", "title": "It's Beginning to Look a Lot Like Christmas"},
    {"file": "song3.mp3", "title": "Jingle Bells"}
]


def play_song_clip(song_file):
    songs.mixer.music.load(song_file)
    songs.mixer.music.play()

    start_time = time.time()
    while songs.mixer.music.get_busy(): 
        if time.time() - start_time > 5:
            songs.mixer.music.stop()
            break
        time.sleep(0.5)
    songs.mixer.music.stop()

def show_song_clip():
    song = songs[0] 
    messagebox.showinfo("Now Playing", f"Now playing: {song['title']}")
    play_song_clip(song["file"])

root = tk.Tk()
root.title("Christmas Song Player")

play_button = tk.Button(root, text="Play Song Clip", command=show_song_clip)
play_button.pack(pady=20)