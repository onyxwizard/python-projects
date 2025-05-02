import tkinter as tk
from tkinter import messagebox

class GameView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        # Create the grid of buttons
        for row in range(3):
            for col in range(3):
                button = tk.Button(
                    self.root,
                    text=" ",
                    font=("Helvetica", 20),
                    width=6,
                    height=3,
                    command=lambda r=row, c=col: self.controller.on_button_click(r, c)
                )
                button.grid(row=row, column=col)
                self.buttons[row][col] = button

    def update_button(self, row, col, player):
        # Update the button text with the player's mark
        self.buttons[row][col].config(text=player)

    def show_message(self, message):
        # Display a message box with the given message
        messagebox.showinfo("Game Over", message)

    def reset_board(self):
        # Reset all buttons to their initial state
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text=" ")