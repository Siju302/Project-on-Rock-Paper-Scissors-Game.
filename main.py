from tkinter import *
from PIL import Image, ImageTk
import random

# Define the options for the game
options = ["Rock", "Paper", "Scissors"]

# Function to simulate the game and handle button clicks
def button_click(player_choice):
    # Computer makes its choice
    computer_choice = random.choice(options)
    
    # Display the computer's choice in the console
    print(f"Computer chose: {computer_choice}")
    
    # Determine the result
    if player_choice == computer_choice:
        result = "It's a tie!"
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        result = "You win!"
    else:
        result = "Computer wins!"
    
    # Update the result label
    result_label.config(text=result)

# Create the main window
root = Tk()
root.title("Rock, Paper, Scissors")

# Adding title label to the window
title_label = Label(root, text="Rock, Paper, Scissors Game")
title_label.pack(pady=20)

# Create a result label to display the outcome of the game
result_label = Label(root, text="")
result_label.pack(pady=10)

# Load the images for the buttons (ensure the images are in the same directory or provide the correct path)
try:
    rock_img = PhotoImage(file="rock.png")
    paper_img = PhotoImage(file="paper.png")
    scissors_img = PhotoImage(file="scissors.png")
except Exception as e:
    print("Error loading images:", e)
    rock_img = paper_img = scissors_img = None

# Create Rock button
rock_button = Button(root, text="Rock", image=rock_img, compound=TOP, command=lambda: button_click("Rock"))
rock_button.pack(side=LEFT, padx=10, pady=10)

# Create Paper button
paper_button = Button(root, text="Paper", image=paper_img, compound=TOP, command=lambda: button_click("Paper"))
paper_button.pack(side=LEFT, padx=10, pady=10)

# Create Scissors button
scissors_button = Button(root, text="Scissors", image=scissors_img, compound=TOP, command=lambda: button_click("Scissors"))
scissors_button.pack(side=LEFT, padx=30, pady=30)

# Run the Tkinter event loop
root.mainloop()