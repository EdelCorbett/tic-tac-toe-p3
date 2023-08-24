import random
import time
import colorama
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


def start_game_board():
    return [["1", "2", "3"],
            ["4", "5", "6"],
            ["7", "8", "9"]]

def check_for_win(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def check_for_tie(board):
    return all(cell in ["X", "O"] for row in board for cell in row)

def computer_move(board):
    empty_cells = [(row, col) for row in range(3) for col in range(3) if board[row][col] not in ["X", "O"]]
    return random.choice(empty_cells) if empty_cells else None

def get_player_name():
    return input("Enter your name (X): ")

def choose_players():
    player_options = ["Player vs. Player", "Player vs. Computer"]
    terminal_menu = TerminalMenu(player_options, title="Tic Tac Toe - Choose Players")
    selected_index = terminal_menu.show()
    if selected_index == 0:
        return "Player vs. Player"
    else:
        return "Player vs. Computer"

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

        current_player = "O" if current_player == "X" else "X"

    play_again = input("Play again (y/n)? ")
    if play_again.lower() == "y":
        play_game()
    else:
        print("Goodbye!")
    

if __name__ == "__main__":
    play_game()