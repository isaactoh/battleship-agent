from queue import Queue
import random

from battleship import Battleship

class SearchAgent:

    def __init__(self):
        self.dia_dirs = [
            (1, 1),
            (1, -1),
            (-1, 1),
            (-1, -1)
        ]

        self.adj_dirs = [
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0)
        ]

    def play(self, board: Battleship):
        moves = 0
        self.visited = set()
        self.queue = Queue()
        self.stack = []

        row = board.rows // 2
        col = board.columns // 2

        while not board.is_game_over():
            moves += 1
            print(f"Move {moves}: {row, col}")
            is_hit = board.play(row, col)
            self.visited.add((row, col))

            if is_hit:
                self.adjacent_search(board, row, col)
            else:
                self.diagonal_search(board, row, col)

            next_move = self.next_move()

            if next_move is not None:
                row, col = next_move
            else:
                row, col = self.rand_move(board)

        print(f"Game won with {moves} moves")
        return moves

    def next_move(self):
        while self.stack:
            move = self.stack.pop()
            if move not in self.visited:
                return move

        while not self.queue.empty():
            move = self.queue.get()
            if move not in self.visited:
                return move

    def adjacent_search(self, board, row, col):
        for dir in self.adj_dirs:
            new_row, new_col = row + dir[0], col + dir[1]
            if board.is_valid_move(new_row, new_col):
                self.stack.append((new_row, new_col))

    def diagonal_search(self, board, row, col):
        for dir in self.dia_dirs:
            new_row, new_col = row + dir[0], col + dir[1]
            if board.is_valid_move(new_row, new_col):
                self.queue.put((new_row, new_col))

    def rand_move(self, board):
        valid_moves = [
            (row, col)
            for row in range(board.rows)
            for col in range(board.columns)
            if board.is_valid_move(row, col)
        ]
        
        row, col = random.choice(valid_moves)
        return row, col