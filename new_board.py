import random
import time
from collections import deque

start_time = time.time()


class NewBoard:
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

    # def reveal_cell(self, row, col):
    #     """Reveals a cell's true value on the board, given the row and column.
    #     Returns 'mine', 'empty', or 'numbered'."""
    #     cells_to_reveal = set()
    #
    #     # If a mine is chosen, reveal and say game over
    #     if self.board_values[row][col] == -1:
    #         self.board_hidden[row][col] = '*'
    #
    #         self.print_board(self.board_hidden)
    #
    #         return 'mine', {(row, col)}
    #         # print("_________________________________")
    #
    #     # If an empty cell is chosen, call the helper to clear adjacent cells
    #     elif self.board_values[row][col] == 0:
    #         cells_to_reveal = self.reveal_empty_cell_helper(row, col)
    #
    #         self.print_board(self.board_hidden)
    #
    #         return 'empty', cells_to_reveal
    #
    #     # If a numbered cell is chosen, reveal it
    #     else:
    #         self.board_hidden[row][col] = str(self.board_values[row][col])
    #
    #         self.print_board(self.board_hidden)
    #
    #         return 'number', {(row, col)}
    #         # self.print_board(self.board_hidden)
    #
    # def reveal_empty_cell_helper(self, row_start, col_start):
    #     """Helper function that uses BFS to reveal all adjacent cells when an empty cell is selected."""
    #
    #     # BFS implementation
    #     # Stop if the chosen cell is a mine
    #     if self.board_values[row_start][col_start] == -1:
    #         return []
    #
    #     visited_coords = set()  # Set up the trackers to make sure that coordinates are not repeated
    #     queue_coords = deque([(row_start, col_start)])  # Creates the queue to search through
    #     cells_to_reveal = []
    #
    #     directions = [
    #         (-1, 0), (1, 0), (0, -1), (0, 1),  # Up, down, left, right
    #         (-1, -1), (-1, 1), (1, -1), (1, 1)  # Diagonals: top-left, top-right, bottom-left, bottom-right
    #     ]
    #
    #     # While there are coordinates to be checked
    #     while queue_coords:
    #         row, col = queue_coords.popleft()   # Check the first one
    #         self.board_hidden[row][col] = str(self.board_values[row][col])  # Reveal the cell on the board
    #
    #         # If we have already checked this coordinate, then move on
    #         if (row, col) in visited_coords:
    #             continue
    #
    #         visited_coords.add((row, col))  # Check off this coordinate in the future
    #         cells_to_reveal.append((row, col))
    #
    #         # If the cell is not an empty cell, then move on
    #         if self.board_values[row][col] != 0:
    #             continue
    #
    #         # Running through all the adjacent cells using directions
    #         for dr, dc in directions:
    #             new_row, new_col = row + dr, col + dc
    #             # If it is in bounds and the cell is currently hidden
    #             if 0 <= new_row < self.rows and 0 <= new_col < self.cols and self.board_hidden[new_row][new_col] == '-':
    #                 queue_coords.append((new_row, new_col)) # Add new coordinates to be checked
    #     # print(visited_coords)
    #     return visited_coords


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


# board = Board(6, 6, 5, seed=42)
# board.generate_board()
# board.reveal_cell(4, 3)
# board.flag_cell(0, 5)
# board.reveal_cell(5, 0)
#
# end_time = time.time()
# duration = end_time - start_time
# print(f"Runtime: {duration:.4f} seconds")
