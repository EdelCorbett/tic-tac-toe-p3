import random
import time
from colorama import Fore,Style
from simple_term_menu import TerminalMenu

PLAYER_COLORS = {"X": Fore.LIGHTYELLOW_EX, "O": Fore.LIGHTBLUE_EX}


def game_board(board):
    border = f"{Fore.RED}---------{Fore.RESET}"
    separator = f"{Fore.RED} | {Fore.RESET}"

    for row in board:
        colored_row = [
            cell if cell in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
            else (f"{Fore.LIGHTYELLOW_EX}{cell}{Fore.RESET}" if cell == "X"
                else f"{Fore.LIGHTBLUE_EX}{cell}{Fore.RESET}") for cell in row]
        
        print(separator.join(colored_row))
        print(border)


def start_game_board():
    return [["1", "2", "3"],
            ["4", "5", "6"],
            ["7", "8", "9"]]

def show_rules():
    rules = [
        " THE RULES OF TIC-TAC-TOE",
        " This game is played on a 9 space board ",
        " Each player takes turns to place their mark (X or O) on the board",
        " The first player to get 3 of their marks in a row wins",
        " They can be up, down, across, or diagonally across the board",
        " If all 9 spaces are full and no one has matched 3 it's a tie",
        " To quit the game press 'q'",
        " To Play again press 'y'",
        " Good Luck!"
    ]

    for rule in rules:
        print(rule)
        time.sleep(1)

def check_for_win(board, player):
    """Checks if the player has won
    by checking all the possible winning combinations
    checks rows columns and diagonals
    """
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
    # if all cells are full and no one has won it's a tie
    return all(cell in ["X", "O"] for row in board for cell in row)
# this function checks for empty cells and returns a random one
# for the computers move and returns a random choice
def computer_move(board):
    empty_cells = [(row, col) for row in range(3) for col in range(3) if board[row][col] not in ["X", "O"]]
    return random.choice(empty_cells) if empty_cells else None

def validate_name(name):
    return name.isalpha() and len(name) > 0
# This function gets the player to input their name
def get_player_name(player_symbol):
    while True:
        name = input(
    f"{Fore.LIGHTGREEN_EX}Enter your name ({player_symbol}): {Style.RESET_ALL}"
).strip()

        if validate_name(name):
            return PLAYER_COLORS[player_symbol] + name.upper() + Style.RESET_ALL
        else:
            print(f"{Fore.RED}Invalid name. Please try again.{Style.RESET_ALL}")


def choose_players():
    """This function chooses how the game will be played
    either player vs player or player vs computer
    """
    player_options = ["Player vs. Player", "Player vs. Computer", "Show Rules"]
    terminal_menu = TerminalMenu(player_options, title="Tic Tac Toe - Choose Players")
    selected_index = terminal_menu.show()

    if selected_index == 0:
        return "Player vs. Player"
    elif selected_index == 1:
        return "Player vs. Computer"
    elif selected_index == 2:
        show_rules()
        input(f"{Fore.LIGHTMAGENTA_EX}Press Enter to continue.{Style.RESET_ALL}")
        return choose_players()
    else:
        print(f"{Fore.GREEN}Goodbye!{Fore.RESET}")
        return None

    
def play_game():
    """This is the main function that runs the game
    it get game mode, player names
    displays the game board
    gets player input
    checks for win or tie
    changes player
    asks if player wants to play again
    gives option to quit
    gets computer move
    give the option to play again
    """
    game_mode = choose_players()

    if game_mode is None:
        return
    
    if game_mode == "Player vs. Player":
        player1_name = get_player_name("X")
        player2_name = get_player_name("O")
        
    else:
        player1_name = get_player_name("X")
        player2_name = "Computer (O)"
    
    board = start_game_board()
    current_player = "X"
# This is the game loop
    while True:
        game_board(board)

        if current_player == "X" or game_mode == "Player vs. Player":
            position = input(
                f"{player1_name if current_player == 'X' else player2_name},"
                f"{Fore.LIGHTMAGENTA_EX
                }Enter a position (1-9), or q to quit game:{Style.RESET_ALL} "
                )

            if position.lower() == 'q':
                print(f"{Fore.GREEN}Goodbye!{Style.RESET_ALL}")
                input(f"{Fore.LIGHTMAGENTA_EX}Press Enter to Return to Game Menu.{Style.RESET_ALL}")
                return choose_players()
                

            if not position.isdigit() or not (1 <= int(position) <= 9):
                print(f"{Fore.RED}Invalid input. Please enter a number between 1 and 9.{Style.RESET_ALL}")
                continue

            position = int(position) - 1
            row, col = divmod(position, 3)

            if board[row][col] in ["X", "O"]:
                print(f"{Fore.LIGHTRED_EX}That position is already occupied. Try again.{Style.RESET_ALL}")
                continue
        else:
            print(f"{Fore.LIGHTBLUE_EX}Wait it's the computer's turn...{Style.RESET_ALL}")
            time.sleep(2)
            row, col = computer_move(board)
        
        board[row][col] = current_player

        if check_for_win(board, current_player):
            game_board(board)
            if game_mode == "Player vs. Computer" and current_player == "O":
                print(f"{Fore.LIGHTBLUE_EX}Computer wins!{Style.RESET_ALL}")
            else:
                print(f"{player1_name if current_player == 'X' else player2_name} wins!")
            break

        if check_for_tie(board):
            game_board(board)
            print(f"{Fore.LIGHTMAGENTA_EX}It's a draw!{Style.RESET_ALl}")
            break
# changes player after each move
        current_player = "O" if current_player == "X" else "X"
# asks player if they want to play again

    play_again = input(f"{Fore.LIGHTMAGENTA_EX}Play again (y/n)?{Style.RESET_ALL}")
    if play_again.lower() == "y":
        play_game()
    else:
        print(f"{Fore.GREEN}Goodbye!{Style.RESET_ALL}")
        return

if __name__ == "__main__":
    play_game()