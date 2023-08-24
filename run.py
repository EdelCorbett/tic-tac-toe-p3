import random
import time
from colorama import Fore
from simple_term_menu import TerminalMenu

def game_board(board):
    border = f"{Fore.RED}---------{Fore.RESET}"
    separator = f"{Fore.RED} | {Fore.RESET}"

    for row in board:
        colored_row = [cell if cell in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
            else (f"{Fore.YELLOW}{cell}{Fore.RESET}" if cell == "X"
                else f"{Fore.BLUE}{cell}{Fore.RESET}") for cell in row]
        print(separator.join(colored_row))
        print(border)

# This fuction create a new game board
# Numbers the cells from 1 to 9
def start_game_board():
    return [["1", "2", "3"],
            ["4", "5", "6"],
            ["7", "8", "9"]]
# This function checks if the player has won
# by checking all the possible winning combinations
def check_for_win(board, player):
    #checks rows
    for row in board:
        if all(cell == player for cell in row):
            return True
# checks columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
# checks diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
# if none of the above is true, return false 
    return False
# This function checks if the game is a tie
def check_for_tie(board):
    # if all cells are full and no one has won it's a tie
    return all(cell in ["X", "O"] for row in board for cell in row)
# this function checks for empty cells and returns a random one
# for the computers move and returns a random choice
def computer_move(board):
    empty_cells = [(row, col) for row in range(3) for col in range(3) if board[row][col] not in ["X", "O"]]
    return random.choice(empty_cells) if empty_cells else None
# This function gets the player to input their name
def get_player_name():
    return input("Enter your name (X): ")
"""
 this function chooses how the game will be played
    either player vs player or player vs computer
    and returns the choice
"""
def choose_players():
    player_options = ["Player vs. Player", "Player vs. Computer"]
    terminal_menu = TerminalMenu(player_options, title="Tic Tac Toe - Choose Players")
    selected_index = terminal_menu.show()
    if selected_index == 0:
        return "Player vs. Player"
    else:
        return "Player vs. Computer"
"""
this function starts the game
it get player to enter their names
tell them their symbols
and starts the game
start the game with player X"""
def play_game():
    game_mode = choose_players()
    
    if game_mode == "Player vs. Player":
        player1_name = input("Enter the name of Player 1 (X): ")
        player2_name = input("Enter the name of Player 2 (O): ")
    else:
        player1_name = input("Enter your name (X): ")
        player2_name = "Computer (O)"
    
    board = start_game_board()
    current_player = "X"
# This is the game loop
    while True:
        game_board(board)

        if current_player == "X" or game_mode == "Player vs. Player":
            position = input(f"{player1_name if current_player == 'X' else player2_name}, enter a position (1-9), or q to quit game: ")

            if position.lower() == 'q':
                print("Goodbye!")
                return  # Exit the game loop and function

            if not position.isdigit() or not (1 <= int(position) <= 9):
                print("Invalid input. Please enter a number between 1 and 9.")
                continue

            position = int(position) - 1
            row, col = divmod(position, 3)

            if board[row][col] in ["X", "O"]:
                print("That position is already occupied. Try again.")
                continue
        else:
            print("Wait it's the computer's turn...")
            time.sleep(2)
            row, col = computer_move(board)
        
        board[row][col] = current_player

        if check_for_win(board, current_player):
            game_board(board)
            if game_mode == "Player vs. Computer" and current_player == "O":
                print("Computer wins!")
            else:
                print(f"{player1_name if current_player == 'X' else player2_name} wins!")
            break

        if check_for_tie(board):
            game_board(board)
            print("It's a draw!")
            break
# changes player after each move
        current_player = "O" if current_player == "X" else "X"
# asks player if they want to play again

    play_again = input("Play again (y/n)? ")
    if play_again.lower() == "y":
        play_game()
    else:
        print("Goodbye!")
    
# This is the main function that runs the game
if __name__ == "__main__":
    play_game()