import random

from battleship import Battleship

class RandomAgent:

    def play(self, board: Battleship):
        moves = 0

        while not board.is_game_over():
            moves = moves+ 1
            valid_moves = [
                (row, col)
                for row in range(board.rows)
                for col in range(board.columns)
                if board.is_valid_move(row, col)
            ]

            row, col = random.choice(valid_moves)
            print(f"Move {moves}: {row, col}")
            board.play(row, col)

        print(f"Game won with {board.moves} moves")
        board.display_board()
        return moves