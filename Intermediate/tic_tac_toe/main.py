# main.py

# Import necessary modules
import tkinter as tk
from controller.game_controller import GameController

if __name__ == "__main__":
    # Initialize the tkinter window
    root = tk.Tk()
    root.title("Tic Tac Toe")

    # Initialize the GameController
    app = GameController(root)

    # Start the tkinter event loop
    root.mainloop()