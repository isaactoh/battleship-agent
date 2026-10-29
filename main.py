from battleship import Battleship
from search_agent import SearchAgent
from tests import placements

def main():
    board = Battleship()

    board.place_ships(placements[0])

    board.display_board()

    agent = SearchAgent()
    agent.play(board)


if __name__ == "__main__":
    main()