from battleship import Battleship
from rand_agent import RandomAgent


def main():
    board = Battleship()

    placements = [
        [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)],
        [(2, 0), (3, 0), (4, 0), (5, 0)],
        [(7, 2), (7, 3), (7, 4)],
    ]

    board.place_ships(placements)

    board.display_board()

    agent = RandomAgent(board)
    agent.play()


if __name__ == "__main__":
    main()