
class Battleship:

    def __init__(self, rows=10, columns=10):
        self.rows = rows
        self.columns = columns
        self.moves = 0

        self.board = [
            [0 for _ in range(columns)]
            for _ in range(rows)
        ]

        self.exposed_board = [
            ["-" for _ in range(columns)]
            for _ in range(rows)
        ]

        # store tiles belonging to each ship
        self.ship_sizes = {}

        # store number of tiles hit so far
        self.ship_hits = {}

    # TODO: implement random placement generator
    def place_ships(self, placements):
        # reset everything first
        self.board = [
            [0 for _ in range(self.columns)]
            for _ in range(self.rows)
        ]

        self.exposed_board = [
            ["-" for _ in range(self.columns)]
            for _ in range(self.rows)
        ]

        self.ship_sizes = {}
        self.ship_hits = {}
        self.moves = 0

        for ship_id, ship in enumerate(placements, start=1):

            if not ship:
                raise ValueError("A ship cannot be empty.")

            # validation
            # TODO: check x or y-axis is the same for all tiles of same ship
            for row, col in ship:
                if not (
                    0 <= row < self.rows
                    and 0 <= col < self.columns
                ):
                    raise ValueError(
                        f"Coordinate out of bounds: {(row, col)}"
                    )

                if self.board[row][col] != 0:
                    raise ValueError(
                        f"Overlapping ship at {(row, col)}"
                    )

            # Place the ship using its index as its ID
            self.ship_sizes[ship_id] = len(ship)
            self.ship_hits[ship_id] = 0

            for row, col in ship:
                self.board[row][col] = ship_id

    def is_valid_move(self, row, col):
        return (
            0 <= row < self.rows
            and 0 <= col < self.columns
            and self.exposed_board[row][col] == "-"
        )

    def play(self, row, col):
        if not self.is_valid_move(row, col):
            print(f"Invalid move: ({row}, {col})")
            return None

        self.moves += 1

        ship_id = self.board[row][col]

        if ship_id != 0:
            self.ship_hits[ship_id] += 1

            # check if ship is sunk
            sunk = (
                self.ship_hits[ship_id]
                == self.ship_sizes[ship_id]
            )

            if sunk:
                # reveal all tiles belonging to sunken ship
                for r in range(self.rows):
                    for c in range(self.columns):
                        if self.board[r][c] == ship_id:
                            self.exposed_board[r][c] = str(ship_id)

                print(f"Hit! Ship {ship_id} sunk!")
            else:
                self.exposed_board[row][col] = "X"
                print(f"Hit!")

            return True

        self.exposed_board[row][col] = "O"
        print("Miss!")
        return False

    
    def display_board(self, show_ships=False):
        board = self.board if show_ships else self.exposed_board

        print("   " + "".join(f"{c:3}" for c in range(self.columns)))

        print("   +" + "---" * self.columns + "+")

        for r in range(self.rows):
            print(f"{r:2} | " + "".join(
                f"{str(cell):3}" for cell in board[r]
            ) + "|")


    def is_game_over(self):
        return (
            bool(self.ship_sizes)
            and all(
                self.ship_hits[ship_id] == size
                for ship_id, size in self.ship_sizes.items()
            )
        )
