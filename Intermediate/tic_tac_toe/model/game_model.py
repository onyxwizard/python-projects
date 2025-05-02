class GameModel:
    def __init__(self):
        self.board = {i: " " for i in range(1, 10)}  # Initialize the board
        self.current_player = "X"

    def make_move(self, position, player):
        if self.board[position] == " ":
            self.board[position] = player

    def check_winner(self):
        # Define winning patterns
        patterns = [
            [1, 2, 3], [4, 5, 6], [7, 8, 9],  # Rows
            [1, 4, 7], [2, 5, 8], [3, 6, 9],  # Columns
            [1, 5, 9], [3, 5, 7]              # Diagonals
        ]

        for pattern in patterns:
            if (
                self.board[pattern[0]] == self.board[pattern[1]] == self.board[pattern[2]]
                and self.board[pattern[0]] != " "
            ):
                return self.board[pattern[0]]  # Return the winning player

        return None  # No winner

    def is_draw(self):
        # Check if all positions are filled and no winner
        return " " not in self.board.values() and self.check_winner() is None

    def reset_game(self):
        # Reset the board and current player
        self.board = {i: " " for i in range(1, 10)}
        self.current_player = "X"