import random
import colorama
from colorama import Fore, Back, Style
from simple_term_menu import TerminalMenu

print("TIC TAC TOE")

# Create a board
def game_board(board):
    border = f"{Fore.RED}---------{Fore.RESET}"
    separator = f"{Fore.RED} | {Fore.RESET}"
# changes the color of num to color of X or O
    for row in board:
        colored_row = [cell if cell in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
                    else (f"{Fore.YELLOW}{cell}{Fore.RESET}" if cell == "X"
                            else f"{Fore.BLUE}{cell}{Fore.RESET}") for cell in row]
        print(separator.join(colored_row))
        print(border)

def start_game_board( ):
    return [["1", "2", "3"], 
            ["4", "5", "6"], 
            ["7", "8", "9"]]


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
    
def play_game():
    game_mode = choose_players()
    if game_mode == "Player vs Player":
        player1_name = input("(X) What's your name?: ")
        player2_name = input("(O) What's your name?: ")
    else:
        player1_name = input("(X) What's your name?: ")
        player2_name = "Computer(O)"
        board = start_game_board()
        current_player = "X"

    while True:
        game_board(board)

        if current_player == "X" or game_mode == "Player vs Player":
            position = input(f"{player1_name if current_player == 'X' else player2_name} choose a position from 1-9, or press q to quit: ")

            if position == "q":
                print("Goodbye!")
                return
            # check if the input is a number and if it is between 1-9
            if not position.isdigit() or not (1 <= int(position) <= 9):
                print("Invalid position Enter a number from 1-9")
                continue
           
           # change the position to an int and subtract 1 to get the index of the position
           # divmod is used to get the row and column of the position
            position = int(position) -1
            row, col = divmod(position, 3)
# check if the position is already taken
            if board[row][col] in ["X", "O"]:
                print("Position already taken go again!")
                continue
            

if __name__ == "__main__":
    play_game()
