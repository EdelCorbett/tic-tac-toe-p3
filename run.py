import random
import colorama
from colorama import Fore, Back, Style

print("TIC TAC TOE")

# Create a board
def print_board(board):
    border = f"{Fore.RED}---------{Fore.RESET}"
    separator = f"{Fore.RED} | {Fore.RESET}"
# changes the color of num to color of X or O
    for row in board:
        colored_row = [cell if cell in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
                    else (f"{Fore.YELLOW}{cell}{Fore.RESET}" if cell == "X"
                            else f"{Fore.BLUE}{cell}{Fore.RESET}") for cell in row]
        print(separator.join(row))
        print(border)

def game_board( ):
    return [["1", "2", "3"], 
            ["4", "5", "6"], 
            ["7", "8", "9"]]
board = game_board()

print_board(board)

