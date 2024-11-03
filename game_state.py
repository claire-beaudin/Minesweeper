# game_state.py
from board import Board

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
        if self.game_over or (row, col) in self.revealed_cells:
            return

        cell_state = self.board.reveal_cell(row, col)

        if cell_state == 'mine':
            self.game_over = True
            print('Game Over!')
            return 'game_over'
        elif cell_state == 'empty':
            # Reveal all connected empty cells
            cells_to_reveal = self.board.reveal_empty_cell_helper(row, col)
            self.revealed_cells.update(cells_to_reveal)  # Add all revealed cells to the revealed set
            for r, c in cells_to_reveal:
                print(f"Revealed empty cell at ({r}, {c})")
        else:
            self.revealed_cells.add((row, col))
            print(f"Revealed numbered cell at ({row}, {col}): {self.board.board_values[row][col]}")

        if self.check_win_condition():
            self.game_over = True
            self.win = True
            print("Congratulations! You've won.")
            return 'win'

        return cell_state

    def flag_cell(self, row, col):
        """Flag or unflag a cell."""
        if self.game_over:
            return  # No action if the game is over

        if (row, col) in self.flagged_cells:
            self.flagged_cells.remove((row, col))  # Unflag if already flagged
            print(f"Unflagged cell at ({row}, {col})")
        else:
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



