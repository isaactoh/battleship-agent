from tests import placements

from battleship import Battleship
from rand_agent import RandomAgent
from search_agent import SearchAgent

def main():
    rand_count = 0
    search_count = 0
    no_games = len(placements)

    game = Battleship()
    rand_agent = RandomAgent()
    search_agent = SearchAgent()

    for i in range(no_games):
        game.place_ships(placements[i])
        rand_count = rand_count + rand_agent.play(game)
        game.place_ships(placements[i])
        search_count = search_count + search_agent.play(game)

    print(f"Random Agent had an average of {rand_count / no_games} moves")
    print(f"Search Agent had an average of {search_count / no_games} moves")

if __name__ == "__main__":
    main()