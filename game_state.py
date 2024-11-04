# game_state.py
from board import Board
from collections import deque



class GameState:
    def __init__(self, rows, cols, num_mines, seed):
        self.rows = rows
        self.cols = cols
        self.num_mines = num_mines
        self.seed = seed
        self.board = Board(rows, cols, num_mines, seed)
        self.revealed_cells = set()  # Track revealed cells
        self.flagged_cells = set()  # Track flagged cells
        self.game_over = False
        self.win = False

    def reveal_cell(self, row, col):
        """Reveal a cell, update game state, and check win/loss."""
        print("self.flagged_cells:", self.flagged_cells)

        if self.game_over or (row, col) in self.flagged_cells or (row, col) in self.revealed_cells:
            return

        cell_state = self.board.board_values[row][col]

        if cell_state == -1:
            self.board.reveal_mine(row, col)
            self.game_over = True
            print("YOU LOST")
        elif cell_state == 0:
            self.revealed_cells.update(self.reveal_empty_cell_helper(row, col))
        else:
            self.board.reveal_num(row, col)
            self.revealed_cells.add((row, col))

        if self.check_win_condition():
            self.game_over = True
            self.win = True
            print("Congratulations! You've won.")
            return 'win'

        # print(cell_state)
        return self.revealed_cells

    def reveal_empty_cell_helper(self, row_start, col_start):
        visited_coords = set()
        queue_coords = deque([(row_start, col_start)])
        cells_to_reveal = []

        directions = [
            (-1, 0), (1, 0), (0, -1), (0, 1),  # Up, down, left, right
            (-1, -1), (-1, 1), (1, -1), (1, 1)  # Diagonals: top-left, top-right, bottom-left, bottom-right
        ]

        while queue_coords:
            r, c = queue_coords.popleft()   # Check the first one
            curr_cell_val = self.board.board_values[r][c]

            # self.board.board_hidden[row][col] = str(self.board.board_values[row][col])  # Reveal the cell on the board
            print(f'new_coords: ({r}, {c})')

            self.board.reveal_num(r, c)


            # If we have already checked this coordinate, then move on
            if (r, c) in visited_coords:
                continue

            visited_coords.add((r, c))  # Check off this coordinate in the future
            cells_to_reveal.append((r, c))

            # If the cell is not an empty cell, then move on
            if curr_cell_val != 0:
                continue

            # Running through all the adjacent cells using directions
            for dr, dc in directions:
                new_row, new_col = r + dr, c + dc
                # print(f'new_coords: ({new_row}, {new_col})')
                # If it is in bounds and the cell is currently hidden
                if 0 <= new_row < self.rows and 0 <= new_col < self.cols and self.board.board_hidden[new_row][new_col] == '-':
                    queue_coords.append((new_row, new_col))  # Add new coordinates to be checked
            print(f'queue_coords: {queue_coords}')
        return visited_coords



    def flag_cell(self, row, col):
        """Flag or unflag a cell."""
        if self.game_over or (row, col) in self.revealed_cells:
            return  # No action if the game is over

        # self.board.flag_cell(row, col)

        print(f'revealed cells: {self.revealed_cells}')


        if (row, col) in self.flagged_cells:
            self.board.unflag_cell(row, col)
            self.flagged_cells.remove((row, col))  # Unflag if already flagged
            print(f"Unflagged cell at ({row}, {col})")
        elif (row, col) not in self.revealed_cells:
            self.board.flag_cell(row, col)
            self.flagged_cells.add((row, col))  # Flag the cell
            print(f"Flagged cell at ({row}, {col})")

    def check_win_condition(self):
        """Check if all non-mine cells are revealed."""
        non_mine_cells = self.rows * self.cols - self.num_mines
        return len(self.revealed_cells) == non_mine_cells

    def reveal_full_board(self):
        """Reveal the entire board (for when the game ends)."""
        self.game_over = True
        full_board = self.board.reveal_full_board()
        print("Final Board:")
        for row in full_board:
            print(" ".join(f"{cell:>3}" for cell in row))

    def reset(self):
        """Reset the game state for a new game."""
        self.revealed_cells.clear()
        self.flagged_cells.clear()
        self.game_over = False
        self.win = False
        self.board = Board(self.rows, self.cols, self.num_mines, self.board.seed)  # Regenerate the board



