import random
import time
from collections import deque

start_time = time.time()


# class Board:
#     def __init__(self, rows, cols, num_mines, seed=None):
#         self.rows = rows
#         self.cols = cols
#         self.num_mines = num_mines
#         self.seed = seed if seed is not None else random.randint(0, 1000000)
#         print(f'Seed used for board generation: {self.seed}')
#         self.board_values = self.generate_board()
#         self.board_hidden = [['-' for _ in range(self.cols)] for _ in range(self.rows)]
#         # self.board_final =
#
#     # Generates the board
#     def generate_board(self):
#         board_values = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
#
#         # if self.seed is not None:
#         #     random.seed(self.seed)
#
#         # Tracks the number of mines left to place
#         mines_to_place = self.num_mines
#
#         # Places the mines according to the seed
#         while mines_to_place > 0:
#             row = random.randint(0, self.rows - 1)
#             col = random.randint(0, self.cols - 1)
#
#             if board_values[row][col] != -1:
#                 board_values[row][col] = -1
#                 mines_to_place -= 1
#
#                 # Places the numbers around the mines
#                 for r in range(-1, 2):
#                     for c in range(-1, 2):
#                         # Checks to see if the coordinates are in bounds. Makes sure that the current coordinate is not a mine
#                         if 0 <= row + r < self.rows and 0 <= col + c < self.cols and board_values[row + r][col + c] != -1:
#                             board_values[row + r][col + c] += 1
#
#         # self.print_board(board_values)
#         # print("________________________________")
#
#         return board_values
#
#     def reveal_cell(self, row, col):
#         # If a mine is chosen, reveal and say game over
#         if self.board_values[row][col] == -1:
#             self.board_hidden[row][col] = '*'
#             # print("_________________________________")
#             # self.print_board(self.board_hidden)
#
#             # !! make sure to call a game over function once I create it
#             print("GAME OVER")
#
#         # If an empty cell is chosen, call the helper to clear adjacent cells
#         elif self.board_values[row][col] == 0:
#             self.reveal_empty_cell_helper(row, col)
#
#         # If a numbered cell is chosen, reveal it
#         else:
#             self.board_hidden[row][col] = str(self.board_values[row][col])
#             # self.print_board(self.board_hidden)
#
#     def reveal_empty_cell_helper(self, row_start, col_start):
#         # # recursive implementation
#         # if 0 > row_start or row_start >= self.rows or 0 > col_start or col_start >= self.cols or self.board_values[row_start][col_start] == -1:
#         #     return
#         # if self.board_hidden[row_start][col_start] != '-':
#         #     return
#         # self.board_hidden[row_start][col_start] = str(self.board_values[row_start][col_start])
#         # if self.board_values[row_start][col_start] == 0:
#         #     self.reveal_empty_cell_helper(row_start - 1, col_start)
#         #     self.reveal_empty_cell_helper(row_start, col_start - 1)
#         #     self.reveal_empty_cell_helper(row_start + 1, col_start)
#         #     self.reveal_empty_cell_helper(row_start, col_start + 1)
#
#         # BFS implementation
#         # Stop if the chosen cell is a mine
#         if self.board_values[row_start][col_start] == -1:
#             return
#
#         visited_coords = set()  # Set up the trackers to make sure that coordinates are not repeated
#         queue_coords = deque([(row_start, col_start)])  # Creates the queue to search through
#
#         directions = [
#             (-1, 0), (1, 0), (0, -1), (0, 1),  # Up, down, left, right
#             (-1, -1), (-1, 1), (1, -1), (1, 1)  # Diagonals: top-left, top-right, bottom-left, bottom-right
#         ]
#
#         # While there are coordinates to be checked
#         while queue_coords:
#             row, col = queue_coords.popleft()   # Check the first one
#             self.board_hidden[row][col] = str(self.board_values[row][col])  # Reveal the cell on the board
#
#             # If we have already checked this coordinate, then move on
#             if (row, col) in visited_coords:
#                 continue
#
#             visited_coords.add((row, col))  # Check off this coordinate in the future
#
#             # If the cell is not an empty cell, then move on
#             if self.board_values[row][col] != 0:
#                 continue
#
#             # Running through all the adjacent cells using directions
#             for dr, dc in directions:
#                 new_row, new_col = row + dr, col + dc
#                 # If it is in bounds and the cell is currently hidden
#                 if 0 <= new_row < self.rows and 0 <= new_col < self.cols and self.board_hidden[new_row][new_col] == '-':
#                     queue_coords.append((new_row, new_col)) # Add new coordinates to be checked
#
#     # Flag the selected cell
#     def flag_cell(self, row, col):
#         self.board_hidden[row][col] = '^'
#         # self.print_board(self.board_hidden)
#
#     # Formats and prints the board so that it is aligned
#     @staticmethod
#     def print_board(b):
#         for row in b:
#             print(" ".join(f"{cell:>3}" for cell in row))
#
#
# # board = Board(6, 6, 5, seed=42)
# # board.generate_board()
# # board.reveal_cell(4, 3)
# # board.flag_cell(0, 5)
# # board.reveal_cell(5, 0)
# #
# # end_time = time.time()
# # duration = end_time - start_time
# # print(f"Runtime: {duration:.4f} seconds")


class Board:
    def __init__(self, rows, cols, num_mines, seed=None):
        self.rows = rows
        self.cols = cols
        self.num_mines = num_mines
        self.seed = seed if seed is not None else random.randint(0, 1000000)
        print(f'Seed used for board generation: {seed}')
        self.board_values = self.generate_board()
        self.board_hidden = [['-' for _ in range(cols)] for _ in range(rows)]
        # self.board_final =
        self.print_board(self.board_values)
        print('_____________________________')

    def generate_board(self):
        """Generate a Minesweeper board with mines and numbers based on the seed."""
        board_values = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

        if self.seed is not None:
            random.seed(self.seed)

        # Tracks the number of mines left to place
        mines_to_place = self.num_mines

        # Places the mines according to the seed
        while mines_to_place > 0:
            row = random.randint(0, self.rows - 1)
            col = random.randint(0, self.cols - 1)

            if board_values[row][col] != -1:
                board_values[row][col] = -1
                mines_to_place -= 1

                # Places the numbers around the mines
                for r in range(-1, 2):
                    for c in range(-1, 2):
                        # Checks to see if the coordinates are in bounds. Makes sure that the current coordinate is not a mine
                        if 0 <= row + r < self.rows and 0 <= col + c < self.cols and board_values[row + r][col + c] != -1:
                            board_values[row + r][col + c] += 1

        # self.print_board(board_values)
        # print("________________________________")

        return board_values

    def reveal_cell(self, row, col):
        """Reveals a cell's true value on the board, given the row and column.
        Returns 'mine', 'empty', or 'numbered'."""
        # If a mine is chosen, reveal and say game over
        if self.board_values[row][col] == -1:
            self.board_hidden[row][col] = '*'
            return 'mine'
            # print("_________________________________")
            # self.print_board(self.board_hidden)

            # !! make sure to call a game over function once I create it
            # print("GAME OVER")

        # If an empty cell is chosen, call the helper to clear adjacent cells
        elif self.board_values[row][col] == 0:
            self.reveal_empty_cell_helper(row, col)
            return 'empty'

        # If a numbered cell is chosen, reveal it
        else:
            self.board_hidden[row][col] = str(self.board_values[row][col])
            return 'number'
            # self.print_board(self.board_hidden)

    def reveal_empty_cell_helper(self, row_start, col_start):
        """Helper function that uses BFS to reveal all adjacent cells when an empty cell is selected."""
        # # recursive implementation
        # if 0 > row_start or row_start >= self.rows or 0 > col_start or col_start >= self.cols or self.board_values[row_start][col_start] == -1:
        #     return
        # if self.board_hidden[row_start][col_start] != '-':
        #     return
        # self.board_hidden[row_start][col_start] = str(self.board_values[row_start][col_start])
        # if self.board_values[row_start][col_start] == 0:
        #     self.reveal_empty_cell_helper(row_start - 1, col_start)
        #     self.reveal_empty_cell_helper(row_start, col_start - 1)
        #     self.reveal_empty_cell_helper(row_start + 1, col_start)
        #     self.reveal_empty_cell_helper(row_start, col_start + 1)

        # BFS implementation
        # Stop if the chosen cell is a mine
        if self.board_values[row_start][col_start] == -1:
            return []

        visited_coords = set()  # Set up the trackers to make sure that coordinates are not repeated
        queue_coords = deque([(row_start, col_start)])  # Creates the queue to search through
        cells_to_reveal = []

        directions = [
            (-1, 0), (1, 0), (0, -1), (0, 1),  # Up, down, left, right
            (-1, -1), (-1, 1), (1, -1), (1, 1)  # Diagonals: top-left, top-right, bottom-left, bottom-right
        ]

        # While there are coordinates to be checked
        while queue_coords:
            row, col = queue_coords.popleft()   # Check the first one
            self.board_hidden[row][col] = str(self.board_values[row][col])  # Reveal the cell on the board

            # If we have already checked this coordinate, then move on
            if (row, col) in visited_coords:
                continue

            visited_coords.add((row, col))  # Check off this coordinate in the future
            cells_to_reveal.append((row, col))

            # If the cell is not an empty cell, then move on
            if self.board_values[row][col] != 0:
                continue

            # Running through all the adjacent cells using directions
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                # If it is in bounds and the cell is currently hidden
                if 0 <= new_row < self.rows and 0 <= new_col < self.cols and self.board_hidden[new_row][new_col] == '-':
                    queue_coords.append((new_row, new_col)) # Add new coordinates to be checked
        return cells_to_reveal

    def flag_cell(self, row, col):
        """Sets a flag on the cell given the row and column."""
        self.board_hidden[row][col] = '^'
        # self.print_board(self.board_hidden)

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


# board = Board(6, 6, 5, seed=42)
# board.generate_board()
# board.reveal_cell(4, 3)
# board.flag_cell(0, 5)
# board.reveal_cell(5, 0)
#
# end_time = time.time()
# duration = end_time - start_time
# print(f"Runtime: {duration:.4f} seconds")
