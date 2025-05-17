"""
main.py: druhý projekt do Engeto Online Python Akademie Tic-tac-toe

author: Markéta Vorlová
email: VorlovaMarketa@seznam.cz
"""

# Uvítací zpráva
def print_welcome_message():
    print("Welcome to Tic Tac Toe")
    print("=" * 43)
    print("GAME RULES:")
    print("Each player can place one mark (or stone)")
    print("per turn on the 3x3 grid. The WINNER is")
    print("who succeeds in placing three of their")
    print("marks in a:")
    print("* horizontal,")
    print("* vertical or")
    print("* diagonal row")
    print("=" * 43)
    print("Let's start the game")

# Zobrazení herního pole
def print_board(board):
    print("-" * 43)
    print("+---+---+---+")
    print(f"| {board[0]} | {board[1]} | {board[2]} |")
    print("+---+---+---+")
    print(f"| {board[3]} | {board[4]} | {board[5]} |")
    print("+---+---+---+")
    print(f"| {board[6]} | {board[7]} | {board[8]} |")
    print("+---+---+---+")
    print("-" * 43)

# Pomocné očíslované pole pro testování
def print_board_debug():
    print("Position reference:")
    print("+---+---+---+")
    print("| 1 | 2 | 3 |")
    print("+---+---+---+")
    print("| 4 | 5 | 6 |")
    print("+---+---+---+")
    print("| 7 | 8 | 9 |")
    print("+---+---+---+")

# Získání a kontrola vstupu hráče
def get_player_move(board, player):
    while True:
        move = input(f"Player {player} | Please enter your move number (1-9): ")

        if not move.isdigit():
            print("Invalid input! Please enter a number.")
            continue

        move = int(move)

        if move < 1 or move > 9:
            print("Invalid number! Please choose from 1 to 9.")
            continue

        if board[move - 1] != " ":
            print("This spot is already taken!")
            continue

        return move - 1

# Kontrola výhry
def check_win(board, player):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # řádky
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # sloupce
        [0, 4, 8], [2, 4, 6]              # diagonály
    ]

    for combo in win_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

# Hlavní herní smyčka
def play_game():
    board = [" " for _ in range(9)]
    current_player = "O"

    print_board_debug()
    print_board(board)

    while True:
        print("=" * 43)
        move_index = get_player_move(board, current_player)
        board[move_index] = current_player
        print_board(board)

        # Kontrola výhry
        if check_win(board, current_player):
            print("=" * 43)
            print(f"Congratulations, the player {current_player} WON!")
            break

        # Kontrola remízy
        if " " not in board:
            print("=" * 43)
            print("It's a tie! No more empty spaces.")
            break

        # Přepnutí hráče
        current_player = "X" if current_player == "O" else "O"

# Spuštění hry
print_welcome_message()
play_game()
