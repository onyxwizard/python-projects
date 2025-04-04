# main.py
class Game:
    def __init__(self):
        self.player1 = None  # Will store "X" or "O"
        self.player2 = None  # Will store "X" or "O"
        self.max_attempt = 2  # Maximum attempts for input validation
        self.board = {
            1: " ", 2: " ", 3: " ",
            4: " ", 5: " ", 6: " ",
            7: " ", 8: " ", 9: " ",
        }
        self.pattern = [
            [1, 2, 3], [4, 5, 6], [7, 8, 9],  # Rows
            [1, 4, 7], [2, 5, 8], [3, 6, 9],  # Columns
            [1, 5, 9], [3, 5, 7]              # Diagonals
        ]
        self.val, self.comment = None, None  # For game logic results

    def board_output(self):
        """Prints the current state of the board."""
        for item in range(0, 7, 3):
            print("------|-------|-----")
            print(f"{item+1} : {self.board.get(item+1)} | {item+2} : {self.board.get(item+2)} | {item+3} : {self.board.get(item+3)}")
        print("------|-------|-----")
    def user_input(self):
        """Handles player symbol selection (X or O)."""
        attempt = 0
        while attempt < self.max_attempt:
            try:
                print("-----------------------------------------------------")
                print("Enter the selection : 'x' or 'o'")
                player1 = input("Enter your selection Player 1 : ").lower()
                if player1 in ['x', 'o']:
                    while True:
                        try:
                            player2 = input("Enter your selection Player 2 : ").lower()
                            if player1 != player2 and player2 in ['x', 'o']:
                                # Assign "X" or "O" directly to players
                                self.player1 = "X" if player1 == "x" else "O"
                                self.player2 = "X" if player2 == "x" else "O"
                                return self.player1, self.player2
                            else:
                                print("Player 2, your selection is wrong.")
                        except ValueError:
                            print("Invalid value")
                else:
                    print("Invalid selection Player 1.")
            except ValueError:
                print("Invalid value")
            attempt += 1
        print("Maximum attempts reached. Exiting game.")
        exit()

    def choice_validation(self):
        """Handles alternating turns between players and checks for win/draw conditions."""
        moves = 0  # Track the total number of moves made
        max_moves = 9  # Maximum moves in Tic-Tac-Toe

        while moves < max_moves:
            print(f"----------{self.val}------{self.comment}----------")
            self.board_output()
            self.choice_validation_player1()
            self.board_output()

            val, comment = self.game_logic()
            if val:
                print(comment)
                break

            moves += 1  # Increment move count after Player 1's turn
            if moves >= max_moves:
                break  # Exit if all positions are filled

            print(f"----------{self.val}------{self.comment}----------")
            self.choice_validation_player2()
            self.board_output()

            val, comment = self.game_logic()
            if val:
                print(comment)
                break

            moves += 1  # Increment move count after Player 2's turn

    def choice_validation_player1(self):
        """Handles Player 1's move input and validates it."""
        attempt = 0
        while attempt < self.max_attempt:
            try:
                player1_move = self.player1_input()
                if self.board[player1_move] == " ":
                    self.board[player1_move] = self.player1
                    return self.board
                else:
                    print("Invalid. Position already taken.")
            except Exception:
                print("Invalid choice value.")
            attempt += 1
        print("Maximum attempts reached. Exiting game.")
        exit()

    def choice_validation_player2(self):
        """Handles Player 2's move input and validates it."""
        attempt = 0
        while attempt < self.max_attempt:
            try:
                player2_move = self.player2_input()
                if self.board[player2_move] == " ":
                    self.board[player2_move] = self.player2
                    return self.board
                else:
                    print("Invalid. Position already taken.")
            except Exception:
                print("Invalid choice value.")
            attempt += 1
        print("Maximum attempts reached. Exiting game.")
        exit()

    def game_logic(self):
        """Checks for win/draw conditions and returns the result."""
        for row in self.pattern:
            # Check if all positions in the row match Player 1's symbol
            if self.board[row[0]] == self.board[row[1]] == self.board[row[2]] == self.player1:
                self.val = True
                self.comment = "Player 1 wins!"
                return self.val, self.comment

            # Check if all positions in the row match Player 2's symbol
            if self.board[row[0]] == self.board[row[1]] == self.board[row[2]] == self.player2:
                self.val = True
                self.comment = "Player 2 wins!"
                return self.val, self.comment

        # Check for a draw (if all positions are filled)
        if all(value != " " for value in self.board.values()):
            self.val = True
            self.comment = "It's a draw!"
            return self.val, self.comment

        # No winner yet
        self.val = False
        self.comment = "Continue"
        return self.val, self.comment

    def player1_input(self):
        """Handles Player 1's input for selecting a position on the board."""
        attempt = 0
        while attempt < self.max_attempt:
            try:
                player1_move = int(input("Enter number on the board Player 1 : "))
                if 1 <= player1_move <= 9:
                    return player1_move
                else:
                    print("Invalid choice. Enter a number between 1 and 9.")
            except ValueError:
                print("Invalid value. Enter a valid number.")
            attempt += 1
        print("Maximum attempts reached. Exiting game.")
        exit()

    def player2_input(self):
        """Handles Player 2's input for selecting a position on the board."""
        attempt = 0
        while attempt < self.max_attempt:
            try:
                player2_move = int(input("Enter number on the board Player 2 : "))
                if 1 <= player2_move <= 9:
                    return player2_move
                else:
                    print("Invalid choice. Enter a number between 1 and 9.")
            except ValueError:
                print("Invalid value. Enter a valid number.")
            attempt += 1
        print("Maximum attempts reached. Exiting game.")
        exit()

    def game_window(self):
        """Main game loop."""
        print("Welcome to Tic Tac Toe!")
        print("---------------------------")
        self.player1, self.player2 = self.user_input()
        print("-----------------------------------------------------")
        self.choice_validation()


if __name__ == "__main__":
    tic = Game()
    tic.game_window()
# # Import necessary modules
# import tkinter as tk
# from controller.game_controller import GameController

# if __name__ == "__main__":
#     # Initialize the tkinter window
#     root = tk.Tk()
#     root.title("Tic Tac Toe")

#     # Initialize the GameController
#     app = GameController(root)

#     # Start the tkinter event loop
#     root.mainloop()