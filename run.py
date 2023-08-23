import random
import colorama
from colorama import Fore, Back, Style
from simple_term_menu import TerminalMenu

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

# Player name input


# Choose play mode computer or player

def choose_players():

    player_options = ["Player vs Player", "Player vs Computer"]
    # Create the terminal menu
    terminal_menu = TerminalMenu(player_options, title="Tic Tac Toe - Choose Players for the Game")
    # Show the menu 
    selected_index = terminal_menu.show()
    # game mode is decided by the index of the selected option
    if selected_index == 0:
        return "Player vs Player"
    else:
        return "Player vs Computer"
    
print(choose_players())

print_board(board)

def play_game():
    game_mode = choose_players()
    if game_mode == "Player vs Player":
        player1_name = input("Player 1, please enter your name (X): ")
        player2_name = input("Player 2, please enter your name (O): ")

    else:
        player1_name = input("Player 1, please enter your name (X): ")
        player2_name = "Computer"
        print(f"{player1_name} vs {player2_name}")

        board = game_board()
        current_player ="X"



