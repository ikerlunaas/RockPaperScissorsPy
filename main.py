import tkinter as tk
import random

user_score = 0
computer_score = 0

def play(user_choice):
    global user_score, computer_score

    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    result = determine_winner(user_choice, computer_choice)

    if result == "You win!":
        user_score += 1
    elif result == "Computer wins!":
        computer_score += 1

    result_label.config(text=f"Computer chose {computer_choice}. {result}")
    update_scores()

def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    if (
        (player == "Rock" and computer == "Scissors")
        or (player == "Paper" and computer == "Rock")
        or (player == "Scissors" and computer == "Paper")
    ):
        return "You win!"
    return "Computer wins!"

def update_scores():
    user_score_label.config(text=f"Your Score: {user_score}")
    computer_score_label.config(text=f"Computer Score: {computer_score}")

# Create the main window
window = tk.Tk()
window.title("Rock, Paper, Scissors Game")

# Create a label for user instructions
instruction_label = tk.Label(window, text="Choose your move:")
instruction_label.pack()

# Create buttons for user choices
rock_button = tk.Button(window, text="Rock", command=lambda: play("Rock"))
paper_button = tk.Button(window, text="Paper", command=lambda: play("Paper"))
scissors_button = tk.Button(window, text="Scissors", command=lambda: play("Scissors"))

rock_button.pack()
paper_button.pack()
scissors_button.pack()

# Create a label for displaying the result
result_label = tk.Label(window, text="")
result_label.pack()

# Create labels for displaying scores
user_score_label = tk.Label(window, text=f"Your Score: {user_score}")
computer_score_label = tk.Label(window, text=f"Computer Score: {computer_score}")
user_score_label.pack()
computer_score_label.pack()

# Start the Tkinter main loop
window.mainloop()
