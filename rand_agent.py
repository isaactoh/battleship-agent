from battleship import Battleship
import random

class RandomAgent:

    def __init__(self, board: Battleship):
        self.board = board
        self.moves = 0

    def play(self):
        while not self.board.is_game_over():
            self.moves = self.moves + 1
            valid_moves = [
                (row, col)
                for row in range(self.board.rows)
                for col in range(self.board.columns)
                if self.board.is_valid_move(row, col)
            ]

            row, col = random.choice(valid_moves)
            print(f"Move {self.moves}: {row, col}")
            self.board.play(row, col)

        print(f"Game won with {self.board.moves} moves")
        self.board.display_board()