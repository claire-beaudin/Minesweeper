import random
import time

start_time = time.time()


class Board:
    def __init__(self, rows, cols, num_mines, seed=None):
        self.rows = rows
        self.cols = cols
        self.num_mines = num_mines
        self.seed = seed if seed is not None else random.randint(0, 1000000)
        print(f'Seed used for board generation: {seed}')
        self.board_values = self.generate_board()
        self.board_hidden = [['-' for _ in range(cols)] for _ in range(rows)]
        self.print_board(self.board_values)
        print('_____________________________')

    def generate_board(self):
        """Generate a Minesweeper board with mines and numbers based on the seed."""
        board_values = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

        if self.seed is not None:
            random.seed(self.seed)

        # Tracks the number of mines left to place
        mines_to_place = self.num_mines
        return self.place_mines(board_values, mines_to_place)

    def place_mines(self, curr_board_vals, to_place):
        new_board_vals = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        while to_place > 0:
            row = random.randint(0, self.rows - 1)
            col = random.randint(0, self.cols - 1)

            if curr_board_vals[row][col] != -1:
                curr_board_vals[row][col] = -1
                to_place -= 1
                new_board_vals = self.place_numbers(curr_board_vals, row, col)

        return new_board_vals

    def place_numbers(self, board_vals, row, col):
        # Places the numbers around the mines
        new_board_vals = board_vals
        for r in range(-1, 2):
            for c in range(-1, 2):
                # Checks to see if the coordinates are in bounds. Makes sure that the current coordinate is not a mine
                if 0 <= row + r < self.rows and 0 <= col + c < self.cols and new_board_vals[row + r][col + c] != -1:
                    new_board_vals[row + r][col + c] += 1
        return new_board_vals

    def reveal_mine(self, row, col):
        self.board_hidden[row][col] = '*'
        self.print_board(self.board_hidden)

    def reveal_empty(self, row, col):
        self.board_hidden[row][col] = '.'
        self.print_board(self.board_hidden)

    def reveal_num(self, row, col):
        self.board_hidden[row][col] = str(self.board_values[row][col])
        self.print_board(self.board_hidden)

    def flag_cell(self, row, col):
        """Sets a flag on the cell given the row and column."""
        self.board_hidden[row][col] = '^'
        self.print_board(self.board_hidden)

    def unflag_cell(self, row, col):
        """Sets a flag on the cell given the row and column."""
        self.board_hidden[row][col] = '-'
        self.print_board(self.board_hidden)

    def reveal_full_board(self):
        """Reveal all cells, showing the full board."""
        final_board = self.board_values
        for row in range(self.rows):
            for col in range(self.cols):
                if self.board_values[row][col] == -1:
                    self.board_hidden[row][col] = '*'
                else:
                    self.board_hidden[row][col] = str(self.board_values[row][col])
        return final_board

    # @staticmethod
    def print_board(self, b):
        """Prints the board in a readable format. Meant for testing"""
        for row in b:
            print(" ".join(f"{cell:>3}" for cell in row))
        print('____________________________')


