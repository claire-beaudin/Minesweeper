# minesweeper_gui.py

import tkinter as tk
from functools import partial
from game_state import GameState  # Import GameState to handle game logic
from board import Board

class MinesweeperGUI:
    def __init__(self, master, rows, cols, num_mines, seed=None):
        self.master = master
        self.rows = rows
        self.cols = cols
        self.game_state = GameState(rows, cols, num_mines, seed)  # Initialize GameState
        self.buttons = [[None for _ in range(cols)] for _ in range(rows)]
        self.create_widgets()

    def create_widgets(self):
        """Create a grid of buttons for each cell in the Minesweeper game."""
        for r in range(self.rows):
            for c in range(self.cols):
                button = tk.Button(self.master, width=3, height=1)
                button.grid(row=r, column=c)

                # Bind left-click (reveal) and right-click (flag) to the same function
                button.bind("<Button-1>", partial(self.cell_clicked, r, c))  # Left-click to reveal
                button.bind("<Button-2>", partial(self.cell_clicked, r, c))  # Right-click to flag
                self.buttons[r][c] = button

    def cell_clicked(self, row, col, event):
        """Handle both left-click and right-click on a cell."""
        if event.num == 1:  # Left-click to reveal
            self.reveal_cell(row, col)
        elif event.num == 2:  # Right-click to flag
            self.flag_cell(row, col)

    def reveal_cell(self, row, col):
        """Reveal a cell and update the GUI based on the game state."""

        # result = self.game_state.board.reveal_cell(row, col)
        # print(result)
        #
        # if result == 'mine':
        #     self.reveal_full_board()
        # elif result == 'empty':
        #     self.buttons[row][col]
        #     # self.show_message("Game Over", "You hit a mine!")

        result = self.game_state.reveal_cell(row, col)
        # print("result:", result)

        if result == 'mine':
            self.reveal_full_board()
            # self.show_message("Game Over", "You hit a mine!")
        # need to implement this
        # something wrong here
        elif self.game_state.check_win_condition():
            self.reveal_full_board()
            # self.show_message("Congratulations", "You've won the game!")
        elif isinstance(result, set):  # Multiple cells to reveal (empty cells and neighbors)
            for r, c in result:
                self.update_button(r, c)
        else:  # Single cell reveal (numbered cell)
            self.update_button(row, col)

        print('___________________________')

    # not working
    def flag_cell(self, row, col):
        """Toggle a flag on right-click."""
        self.game_state.flag_cell(row, col)  # Use GameState for flagging logic
        button = self.buttons[row][col]
        if (row, col) in self.game_state.flagged_cells:
            button.config(text="🚩")  # Set flag icon
        else:
            button.config(text="")  # Remove flag icon

    def update_button(self, row, col):
        """Update the button text based on the revealed cell's value."""
        cell_value = self.game_state.board.board_values[row][col]
        button = self.buttons[row][col]
        if cell_value == -1:
            button.config(text="💣", bg="red")  # Display mine
        elif cell_value == 0:
            button.config(text=".", relief=tk.SUNKEN)  # Empty cell
        else:
            button.config(text=str(cell_value), relief=tk.SUNKEN)  # Numbered cell

    def reveal_full_board(self):
        """Reveal the entire board when the game ends."""
        for r in range(self.rows):
            for c in range(self.cols):
                self.update_button(r, c)
                self.buttons[r][c].config(state="disabled")  # Disable all buttons

    # not working
    # def show_message(self, title, message):
    #     """Display a pop-up message for game over or win."""
    #     tk.messagebox.showinfo(title, message)
