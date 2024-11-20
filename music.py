import pygame
import time
import tkinter as tk
from tkinter import messagebox
import random

pygame.mixer.init()

songs = [
    {"file": "song1.mp3", "title": "Last Christmas"},
    {"file": "song2.mp3", "title": "It's Beginning to Look a Lot Like Christmas"},
    {"file": "song3.mp3", "title": "Jingle Bells"}
]


# Shuffle the songs (optional, to randomize the order)
random.shuffle(songs)

# Function to play a short clip of a song
def play_song_clip(song_file):
    pygame.mixer.music.load(song_file)
    pygame.mixer.music.play()
    # Play for a short period (e.g., 5 seconds)
    time.sleep(5)  # Adjust this time to suit the length of your song clip
    pygame.mixer.music.stop()


