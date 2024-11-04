# # import random
# # import tkinter as tk
# # from functools import partial
# #
# #
# #
# #
# #
# #
# # class MinesweeperGUI:
# #     def __init__(self, master, rows, cols, num_mines, seed):
# #         self.master = master
# #         self.rows = rows
# #         self.cols = cols
# #         self.num_mines = num_mines
# #         self.board = generate_board(rows, cols, num_mines, seed)
# #         self.buttons = [[None for _ in range(cols)] for _ in range(rows)]
# #         self.create_widgets()
# #
# #     def create_widgets(self):
# #         for r in range(self.rows):
# #             for c in range(self.cols):
# #                 button = tk.Button(self.master, width=2, height=1, command=partial(self.reveal_cell, r, c))
# #                 button.bind("<Button-3>", partial(self.flag_cell, r, c))  # Right-click to flag
# #                 button.grid(row=r, column=c)
# #                 self.buttons[r][c] = button
# #
# #     def reveal_cell(self, row, col):
# #         # Reveal cell logic goes here
# #         cell_value = self.board[row][col]
# #         if cell_value == -1:
# #             self.buttons[row][col].config(text="💣", bg="red")  # Reveal a mine
# #             self.game_over(False)
# #         else:
# #             self.buttons[row][col].config(text=str(cell_value), state="disabled", relief=tk.SUNKEN)
# #             # Additional logic could reveal neighboring cells if the value is 0
# #
# #     def flag_cell(self, row, col, event):
# #         # Toggle flag on right-click
# #         button = self.buttons[row][col]
# #         if button["text"] == "🚩":
# #             button.config(text="")
# #         else:
# #             button.config(text="🚩")
# #
# #     def game_over(self, won):
# #         # End game routine
# #         msg = "You Win!" if won else "Game Over"
# #         for row in self.buttons:
# #             for button in row:
# #                 button.config(state="disabled")  # Disable all buttons
# #         tk.messagebox.showinfo("Game Over", msg)
# #
# # # Example usage
# # root = tk.Tk()
# # game = MinesweeperGUI(root, rows=10, cols=10, num_mines=10, seed=42)
# # root.mainloop()
# # main.py
#
# # Step 1: Import the necessary modules and classes
# from board import Board  # Assuming your Board class and related functions are in board.py
# import time
#
#
# # # Step 2: Define any helper functions if necessary
# # def display_board(board):
# #     """Function to print the board in a user-friendly way."""
# #     for row in board:
# #         print(" ".join(row))
#
#
# # Step 3: Set up the game
# def initialize_game():
#     # Game settings
#     rows = 6  # Number of rows
#     cols = 6  # Number of columns
#     num_mines = 1  # Number of mines
#     seed = None  # Optional: use None for random boards
#
#     # Initialize the board
#     game_board = Board(rows, cols, num_mines, seed)
#     # game_board.print_board(game_board.board_values)
#     return game_board
#
#
# # Step 4: Main game loop
# def game_loop(board):
#     """The main loop to handle user moves and display the board."""
#     game_over = False
#
#     while not game_over:
#         # Display the hidden board to the player
#         print("\nCurrent Board:")
#         Board.print_board(board.board_hidden)
#
#         # Get user input (for interactive games)
#         try:
#             row = int(input("Enter row to reveal: "))
#             col = int(input("Enter column to reveal: "))
#         except ValueError:
#             print("Invalid input. Please enter numbers.")
#             continue
#
#         # Reveal cell and check for win/loss
#         # board.reveal_empty_cell_helper(row, col)  # Use your reveal function
#         # if board.board_values[row][col] == -1:
#         #     print("Boom! You hit a mine!")
#         #     game_over = True
#         # else:
#         #     # Check for win condition if all non-mine cells are revealed
#         #     game_over = check_win_condition(board)
#
#         board.reveal_cell(row, col)
#
#     # Show the final board after the game ends
#     print("\nFinal Board:")
#     board.print_board(board.board_values)
#
#
# # Optional: Define a function to check win condition
# def check_win_condition(board):
#     """Check if all non-mine cells have been revealed."""
#     for r in range(board.rows):
#         for c in range(board.cols):
#             if board.board_values[r][c] != -1 and board.board_hidden[r][c] == '-':
#                 return False  # Game is not won yet
#     print("Congratulations! You've revealed all safe cells!")
#     return True
#
#
# # Step 5: Define the main entry point
# if __name__ == "__main__":
#     # Initialize the game
#     board = initialize_game()
#
#     # Start the game loop
#     game_loop(board)


# main.py

from game_state import GameState
import tkinter as tk
from minesweeper_gui import MinesweeperGUI  # Import the MinesweeperGUI class

def game_loop():
    rows, cols, num_mines = 10, 10, 10
    seed = 42
    game_state = GameState(rows, cols, num_mines, seed)

    while not game_state.game_over:
        game_state.board.print_board(game_state.board.board_hidden)  # For debugging
        action = input("Enter 'r' to reveal, 'f' to flag, or 'q' to quit: ").strip().lower()

        if action == 'q':
            break

        # row, col = map(int, input("Enter row and column (e.g., '0 0'): ").split())

        row, col = get_valid_input()

        if action == 'r':
            result = game_state.reveal_cell(row, col)
            if result == 'game_over':
                game_state.reveal_full_board()
            elif result == 'win':
                game_state.reveal_full_board()
        elif action == 'f':
            game_state.flag_cell(row, col)

    if game_state.win:
        print("You won the game!")
    else:
        print("Game Over! Try again.")


def get_valid_input():
    while True:
        try:
            # Prompt user for row and column input
            row, col = map(int, input("Enter row and column (e.g., '0 0'): ").split())
            return row, col  # Return if valid input is entered
        except ValueError:
            # Catch ValueError if input can't be converted to integers
            print("Invalid input. Please enter two integers separated by a space.")

# main.py


def main():
    # Initialize Tkinter window
    root = tk.Tk()
    root.title("Minesweeper")

    # Game configuration: set rows, cols, mines, and optional seed
    rows, cols, num_mines, seed = 5, 5, 5, 42  # Adjust these values as needed

    # Initialize the Minesweeper GUI with the Tkinter window and game settings
    app = MinesweeperGUI(root, rows, cols, num_mines, seed)

    # Start the Tkinter main loop
    root.mainloop()


if __name__ == "__main__":
    main()
    # game_loop()

