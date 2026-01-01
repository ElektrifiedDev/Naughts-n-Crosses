from colorama import Fore, Style, init
import random
import os
import sys
import time
import shutil

init(autoreset=True)

THEME = {
    "X": Fore.RED + "X" + Style.RESET_ALL,
    "O": Fore.BLUE + "O" + Style.RESET_ALL,
    " ": " "
}   

def create_board():
    row1 = [" ", " ", " "]
    row2 = [" ", " ", " "]
    row3 = [" ", " ", " "]
    board = [row1, row2, row3]
    return board

def user_move(board):
    while True:
        move = input(Fore.CYAN + "Enter your move (1-9): ")
        if move not in [str(i) for i in range(1, 10)]:
            print(Fore.RED + "Invalid input. Please enter a number between 1 and 9.")
            continue
        move = int(move) - 1
        row, col = divmod(move, 3)
        if board[row][col] != " ":
            print(Fore.RED + "Cell already taken. Choose another one.")
            continue
        board[row][col] = "X"
        break

def computer_move(board):
    while True:
        move = random.randint(0, 8)
        row, col = divmod(move, 3)
        if board[row][col] == " ":
            board[row][col] = "O"
            break

def check_winner(board):
    winning_combinations = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)],
    ]
    for combination in winning_combinations:
        symbols = [board[r][c] for r, c in combination]
        # Compare against plain strings "X" and "O"
        if symbols == ["X", "X", "X"]:
            return "User"
        if symbols == ["O", "O", "O"]:
            return "Computer"
    return None

def check_tie(board):
    for row in board:
        if " " in row:
            return False
    return True

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_board(board):
    clear_screen()
    print(Fore.GREEN + "Tic Tac Toe")
    print()
    for row in board:
        display_row = [THEME[cell] for cell in row]
        print(" | ".join(display_row))
        print("-" * 9)

def main():
    board = create_board()
    print_board(board)
    while True:
        user_move(board)
        print_board(board)
        if check_winner(board) == "User":
            print(Fore.GREEN + "Congratulations! You win!")
            input()
            break
        if check_tie(board):
            print(Fore.YELLOW + "It's a tie!")
            input()
            break
        time.sleep(1)   
        computer_move(board)
        print_board(board)
        if check_winner(board) == "Computer":
            print(Fore.RED + "Computer wins! Better luck next time.")
            input()
            break
        if check_tie(board):
            print(Fore.YELLOW + "It's a tie!")
            input()
            break

if __name__ == "__main__":
    main()