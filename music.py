import pygame # type: ignore
import time
import tkinter as tk
from tkinter import messagebox
import json

pygame.mixer.init()

songs = [
    {"file": "song1.mp3", "title": "Last Christmas"},
    {"file": "song2.mp3", "title": "It's Beginning to Look a Lot Like Christmas"},
    {"file": "song3.mp3", "title": "Jingle Bells"}
]


json.shuffle(songs)

def play_song_clip(song_file):
    pygame.mixer.music.load(song_file)
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
    messagebox.showinfo("Now Playing", f"Now playing: {song['title']}")
    play_song_clip(song["file"])

root = tk.Tk()
root.title("Christmas Song Player")

play_button = tk.Button(root, text="Play Song Clip", command=show_song_clip)
play_button.pack(pady=20)