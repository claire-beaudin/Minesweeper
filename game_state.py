# game_state.py

class GameState:
    def __init__(self, rows, cols, num_mines):
        self.rows = rows
        self.cols = cols
        self.num_mines = num_mines
        self.revealed_cells = set()  # Track revealed cells
        self.flagged_cells = set()  # Track flagged cells
        self.game_over = False
        self.win = False

    def reveal_cell(self, row, col, board):
        """Reveal a cell, update game state, and check win/loss."""


    def flag_cell(self, row, col):
        """Flag or unflag a cell."""


    def check_win_condition(self, board):
        """Check if all non-mine cells are revealed."""


    def reset(self):
        """Reset the game state for a new game."""

