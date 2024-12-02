import time
import json
import random
import pygame
import tkinter as tk
from tkinter import messagebox, ttk
import ttkbootstrap
from ttkbootstrap import Style
from tkinter import messagebox
x=0
with open("songs.json", "r") as f:
    songs = json.load(f)

with open("questions.json", "r") as f:
    questions = json.load(f)

# Function to display the current question and choices
def show_question():
    # Get the current question from the questions list
    question = questions[current_question]
    question_label.config(text= question['question'])

    # Display the choices on the buttons
    choices = questions[x]['options']
    for i in range(4):
        choice_btns[i].config(text=choices[i], state="normal") # Reset button state

    # Clear the feedback label and disable the next button
    feedback_label.config(text="")
    next_btn.config(state="disabled")

# Function to check the selected answer and provide feedback
def check_answer(choice):
    # Get the current question from the questions list
    question = questions[current_question]
    selected_choice = choice_btns[choice].cget("text")

    # Check if the selected choice matches the correct answer
    if selected_choice == question["answer"]:
        # Update the score and display it
        global score
        score += 1
        score_label.config(text="Score: {}/{}".format(score, len(questions)))
        feedback_label.config(text="Correct!", foreground="green")
    else:
        feedback_label.config(text="Incorrect!", foreground="red")
    
    # Disable all choice buttons and enable the next button
    for button in choice_btns:
        button.config(state="disabled")
    next_btn.config(state="normal")

# Function to move to the next question
def next_question():
    global current_question
    current_question +=1

    if current_question < len(questions):
        # If there are more questions, show the next question
        show_question()
    else:
        # If all questions have been answered, display the final score and end the quiz
        messagebox.showinfo("Quiz Completed",
                            "Quiz Completed! Final score: {}/{}".format(score, len(questions)))
        root.destroy()


root = tk.Tk()
root.title("Quiz App")
root.geometry("600x500")
style = Style(theme="flatly")

question_label = ttk.Label(  root,
    anchor="center",
    wraplength=500,
    padding=10
)
question_label.pack(pady=10)

# Create the choice buttons
choice_btns = []
for i in range(4):
    button = ttk.Button(
        root,
        command=lambda i=i: check_answer(i)
    )
    button.pack(pady=5)
    choice_btns.append(button)


feedback_label = ttk.Label(
    root,
    anchor="center",
    padding=10
)
feedback_label.pack(pady=10)

# Initialize the score
score = 0

# Create the score label
score_label = ttk.Label(
    root,
    text="Score: 0/{}".format(len(questions)),
    anchor="center",
    padding=10
)
score_label.pack(pady=10)


next_btn = ttk.Button(
    root,
    text="Next",
    command=next_question,
    state="disabled"
)
next_btn.pack(pady=10)

current_question = 0







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







































""" print('Imported')
def show_song_clip():
    song = songs[0] 
    messagebox.showinfo("Now Playing", f"Now playing: {song['title']}")
    play_song_clip(song["file"])

root = tk.Tk()
root.title("Pack Example")

# Create three buttons
button1 = tk.Button(root, text="Button 1")
button2 = tk.Button(root, text="Button 2")
button3 = tk.Button(root, text="Button 3")

# Pack the buttons vertically
button1.place(x=600, y=250)
button2.place(x=0, y=550)
button3.place(x=600, y=10)
root.title("Christmas Song Player")

root.mainloop()
 """
play_button = tk.Button(root, text="Play Song Clip", command=play_song_clip)
play_button.pack(pady=20)

show_question()

root.mainloop()
root.mainloop()