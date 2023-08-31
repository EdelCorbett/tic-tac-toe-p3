import random
import os
import time
from colorama import Fore, Style
from simple_term_menu import TerminalMenu


""" This gives X and O different colors"""
PLAYER_COLORS = {"X": Fore.LIGHTYELLOW_EX, "O": Fore.LIGHTBLUE_EX}


def game_board(board):
    """""
    This function displays the game board
    in color using colorama
    and colors the players symbols
    """
    border = f"{Fore.RED}---------{Fore.RESET}"
    separator = f"{Fore.RED} | {Fore.RESET}"

    for row in board:
        colored_row = [
            cell if cell in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
            else (f"{Fore.LIGHTYELLOW_EX}{cell}{Fore.RESET}"
                if cell == "X" else f"{Fore.LIGHTBLUE_EX}{cell}{Fore.RESET}")
            for cell in row]
        print(separator.join(colored_row))
        print(border)


def start_game_board():
    """
    This function creates the game board in grid format number 1-9
    """
    return [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"]
        ]


def show_rules():
    """
    This function displays the rules of the game
    and gives a 1 second delay between each rule
    for easy readability
    """

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


def clear_screen():
    """This function clears the screen"""
    os.system("cls" if os.name == "nt" else "clear")


def check_for_win(board, player):
    """
    Checks if the player has won
    by checking all the possible winning combinations
    checks rows columns and diagonals
    """

    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
        if all(board[i][i] == player for i in range(
                3)) or all(board[i][2 - i] == player for i in range(3)):
            return True
    return False


def check_for_tie(board):
    """Checks if the game is a tie"""
    return all(cell in ["X", "O"] for row in board for cell in row)


def computer_move(board):
    """
    This function gets the computer to make a move
    it checks if cell is empty
    if empty it returns a random cell
    """
    empty_cells = [(row, col) for row in range(
        3) for col in range(3) if board[row][col] not in ["X", "O"]]
    return random.choice(empty_cells) if empty_cells else None


def validate_name(name):
    """
    This function validates the player's name
    checking if name is alphabetic and less than 10 characters
    """
    return name.isalpha() and len(name) <= 10


def get_player_name(player_symbol):
    """
    This function gets the player's name
    and validates it using the validate_name function
    if not valid it asks for name again
    """
    while True:
        name = input(
                f"""{Fore.LIGHTGREEN_EX}Enter your name ({player_symbol}):
                    {Style.RESET_ALL}""").strip()

        if validate_name(name):
            return PLAYER_COLORS[player_symbol] + name.upper(
                ) + Style.RESET_ALL
        else:
            print(f"""{Fore.RED}Invalid name. Please try again.
            {Style.RESET_ALL}""")
            print()


def choose_players():
    """
    This function chooses how the game will be played
    either player vs player or player vs computer or display rules
    from a terminal menu
    """
    player_options = ["Player vs. Player", "Player vs. Computer", "Show Rules"]
    terminal_menu = TerminalMenu(
        player_options, title="Tic Tac Toe Please Choose Players")
    selected_index = terminal_menu.show()

    if selected_index == 0:
        return "Player vs. Player"
    elif selected_index == 1:
        return "Player vs. Computer"
    elif selected_index == 2:
        show_rules()
        input(
            f"{Fore.LIGHTMAGENTA_EX}Press Enter to continue.{Style.RESET_ALL}")
        return choose_players()
    else:
        print(f"{Fore.GREEN}Goodbye!{Fore.RESET}")
        return None


def play_game():
    """
    This is the main function that runs the game
    it get game mode and player names
    displays the game board
    gets player input
    checks for win or tie
    changes player after each move
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

    clear_screen()

    while True:

        game_board(board)

        if current_player == "X" or game_mode == "Player vs. Player":
            position = input(f"""{player1_name if current_player == 'X'
            else
                player2_name},{Fore.LIGHTMAGENTA_EX} Enter position (1-9),
                or q to quit game:
                        {Style.RESET_ALL}""")
            print()

            if position.lower() == "q":
                confirm = input("ARE YOU SURE YOU WANT TO QUIT (y/n)?")
                print()

                if confirm.lower() == "y":
                    print(f"{Fore.GREEN}Goodbye!{Style.RESET_ALL}")
                    time.sleep(1)
                    clear_screen()
                    return play_game()

                elif confirm.lower() == "n":
                    continue

                else:
                    confirm.lower() not in ["y", "n"]
                    print(f"""{Fore.RED}
                        Invalid input.
                        {Style.RESET_ALL}""")
                    print()
                    continue

                    # Checks if input is a number and between 1 and 9
                    # if not it asks for input again
            if not position.isdigit() or not (1 <= int(position) <= 9):
                print(f"""{Fore.RED}
                    Invalid input. Please enter a number between 1 and 9.
                    {Style.RESET_ALL}""")
                print()
                continue

            # Int is making sure the input is a number
            # Divmod is used to get the row and column
            # from the position entered by the player
            # -1 is used to get the correct index
            # Then checks if the position is already occupied
            # if occupied it asks for input again

            position = int(position) - 1
            row, col = divmod(position, 3)

            if board[row][col] in ["X", "O"]:
                print(f"""
                    {Fore.LIGHTRED_EX}Position already occupied.
                    Try again.{Style.RESET_ALL}""")
                print()
                continue
        else:
            print(f"""
                {Fore.LIGHTBLUE_EX}Wait it's the computer's turn...
                {Style.RESET_ALL}""")
            print()
            time.sleep(2)
            row, col = computer_move(board)

        board[row][col] = current_player

        if check_for_win(board, current_player):
            game_board(board)
            if game_mode == "Player vs. Computer" and current_player == "O":
                print(f"{Fore.LIGHTBLUE_EX}Computer wins!{Style.RESET_ALL}")
            else:
                print(f"""{player1_name if current_player == 'X'
                        else player2_name} wins!""")
            break

        if check_for_tie(board):
            game_board(board)
            print(f"{Fore.LIGHTMAGENTA_EX}It's a draw!{Style.RESET_ALL}")
            break

        current_player = "O" if current_player == "X" else "X"

    while True:
        play_again = input(f"""{Fore.LIGHTMAGENTA_EX}Play again (y/n)?
        {Style.RESET_ALL}""").lower()

        if play_again == "y":
            clear_screen()
            return play_game()
        elif play_again == "n":
            print(f"{Fore.GREEN}Goodbye!{Style.RESET_ALL}")
            time.sleep(1)
            clear_screen()
            return play_game()
        else:
            print(f"""{Fore.RED}Invalid input. Please enter y or n.
            {Style.RESET_ALL}""")
            continue


if __name__ == "__main__":
    play_game()
