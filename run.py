import random
import colorama
from colorama import Fore, Back, Style

print("TIC TAC TOE")

# Create a board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("---------")

def game_board( ):
    return [["1", "2", "3"], 
            ["4", "5", "6"], 
            ["7", "8", "9"]]
board = game_board()

print_board(board)

