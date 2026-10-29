from battleship import Battleship

def main():
    game = Battleship()
    game.display_board()

    game.place_ships([
        [(0,0), (0,1), (0,2)],
        [(5,5), (6,5)],
        [(3,6), (3,7), (3,8), (3,9)]
    ])

    while not game.is_game_over():
        print("Enter Next Move", flush=True)
        row = int(input("Row: "))
        col = int(input("Column: "))
        game.play(row, col)

    print(f"Game won with {game.moves} moves")

if __name__ == "__main__":
    main()