import os

class Board():
    def __init__(self):
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]


    def display(self):
        print(f" {self.cells[1]} | {self.cells[2]} | {self.cells[3]} ")
        print("-----------")
        print(f" {self.cells[4]} | {self.cells[5]} | {self.cells[6]} ")
        print("-----------")
        print(f" {self.cells[7]} | {self.cells[8]} | {self.cells[9]} ")


    def update(self, cell_no, player):
        if self.cells[cell_no] == " ":
            self.cells[cell_no] = player


    def is_winner(self, player):
        moves = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 5, 9], [3, 5, 7], [1, 4, 7], [2, 5, 8], [3, 6, 9]]

        for option in moves:
            result = True
            for n in option:
                if self.cells[n] != player:
                    result = False

            if result == True:
                return True

        return False


    def is_tie(self):
        used_cells = 0
        for cell in self.cells:
            if cell != " ":
                used_cells += 1
        if used_cells == 9:
            return True
        else:
            return False


    def reset(self):
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]



board = Board()

def print_welcome():
    print("Welcome to Tic Tac Toe game\n")

def refresh_screen():
    # Clear the screen
    os.system("clear")

    # Print welcome message
    print_welcome()

    # Show the board
    board.display()

while True:
    refresh_screen()

    # Get X input
    x_choice = int(input("Enter X choice from 1 - 9. : "))

    # Update board
    board.update(x_choice, "X")

    # Refresh screen
    refresh_screen()

    # Check for X win
    if board.is_winner("X"):
        print("\n X wins!. \n")
        play_again = input("Would you like to play again? (Y/N) : ").upper()
        if play_again == "Y":
            board.reset()
            continue
        else:
            break

    # Check for tie
    if board.is_tie():
        print("\n Tie game! \n")
        play_again = input("Would you like to play again? (Y/N) : ").upper()
        if play_again == "Y":
            board.reset()
            continue
        else:
            break

    # Get O input
    o_choice = int(input("Enter O choice from 1 - 9. : "))

    # Update board
    board.update(o_choice, "O")

    # Check for O win
    if board.is_winner("O"):
        print("\n O wins!. \n")
        play_again = input("Would you like to play again? (Y/N) : ").upper()
        if play_again == "Y":
            board.reset()
            continue
        else:
            break

    # Check for tie
    if board.is_tie():
        print("\n Tie game! \n")
        play_again = input("Would you like to play again? (Y/N) : ").upper()
        if play_again == "Y":
            board.reset()
            continue
        else:
            break