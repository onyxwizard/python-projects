from model.game_model import GameModel
from view.game_view import GameView


class GameController:
    def __init__(self, root):
        self.model = GameModel()
        self.view = GameView(root, self)
        self.current_player = "X"

    def on_button_click(self, row, col):
        # Get the position on the board
        position = row * 3 + col + 1

        # Make a move if the position is empty
        if self.model.board[position] == " ":
            self.model.make_move(position, self.current_player)
            self.view.update_button(row, col, self.current_player)

            # Check for a winner or draw
            winner = self.model.check_winner()
            if winner:
                self.view.show_message(f"Player {winner} wins!")
                self.reset_game()
            elif self.model.is_draw():
                self.view.show_message("It's a draw!")
                self.reset_game()
            else:
                # Switch players
                self.current_player = "O" if self.current_player == "X" else "X"

    def reset_game(self):
        # Reset the game state in the Model
        self.model.reset_game()

        # Reset the View
        self.view.reset_board()

        # Reset the current player
        self.current_player = "X"