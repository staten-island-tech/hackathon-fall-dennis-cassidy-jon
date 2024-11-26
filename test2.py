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
    {"file": "song1.mp3", "name": "Last Christmas"},
    {"file": "song2.mp3", "name": "Jingle Bells"},
    {"file": "song3.mp3", "name": "It's Beginning to Look a Lot Like Christmas"},
    {"file": "song4.mp3", "name": "Jingle Bell Rock"},
    {"file": "song5.mp3", "name": "All I Want for Christmas is You"},
    {"file": "song6.mp3", "name": "Let it Snow!"},            
       ]


def play_song_clip(song_file):
    try:
        pygame.mixer.music.load(song_file)  
        pygame.mixer.music.play()
    except pygame.error as e:
        print(f"Error loading or playing the song: {e}")
        return

    start_time = time.time()
    while pygame.mixer.music.get_busy():  
        if time.time() - start_time > 5: 
            pygame.mixer.music.stop()
            break
        time.sleep(0.5)

    pygame.mixer.music.stop()

def show_song_clip():
    song = songs[0]  
    messagebox.showinfo("Now Playing")
    play_song_clip(song["file"]) 


root = tk.Tk()
root.title("Christmas Song Player")

play_button = tk.Button(root, text="Play Song Clip", command=show_song_clip)
play_button.pack(pady=20)

root.mainloop()
