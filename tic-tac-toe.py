from random import randint

# X = vez do jogador | O = vez do PC
player_turn = "X"

# -1 = Disponível o espaço | 0 = PC jogou na posicao
# 1 = Jogador jogou na posicao
table = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]

win_game = False


def game_alive() -> bool:
    """Verifica se existe espaco em branco disponivel para jogar.

    Returns:
        bool: True caso ainda seja possivel jogar, False caso nao seja mais possivel jogar.
    """
    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j] == "_":
                return True

    return False


def display_game_table():
    """Exibe a tabela"""
    for i in range(len(table)):
        print(table[i][0], table[i][1], table[i][2], sep=" | ")


def is_valid_position(line: int, col: int) -> bool:
    """Verifica se uma posicao na tabela e valida

    Args:
        line (int): Valor da linha
        col (int): Valor da coluna

    Returns:
        bool: True caso a posicao esteja disponivel
    """
    if line < 0 or line > 2:
        return False

    if col < 0 or col > 2:
        return False

    if table[line][col] == "_":
        return True
    else:
        return False


def verify_win_game(player):
    # Verificacao na horizontal = X X X
    for i in range(len(table)):
        if table[i][0] == player and table[i][1] == player and table[i][2] == player:
            return True

    # Verificacao na vertical
    for i in range(len(table)):
        if table[0][i] == player and table[1][i] == player and table[2][i] == player:
            return True

    # Verifica na diagonal
    if (table[0][0] == player and table[1][1] == player and table[2][2] == player) or (
        table[0][2] == player and table[1][1] == player and table[2][0] == player
    ):
        return True

    return False


def play_player_turn():
    line = int(input("Informe  um valor para a linha: "))
    col = int(input("Informe  um valor para a coluna: "))

    while not is_valid_position(line, col):
        print("Posicao nao e valida, amigao. Tente novamente")
        line = int(input("Informe  um valor para a linha: "))
        col = int(input("Informe  um valor para a coluna: "))

    return line, col


def play_pc_turn():
    line = randint(0, 2)
    col = randint(0, 2)

    while not is_valid_position(line, col):
        line = randint(0, 2)
        col = randint(0, 2)

    return line, col


def display_win_game():
    if verify_win_game(player_turn):
        if player_turn == "X":
            print("Jogador ganhou")
            return True
        else:
            print("PC Ganhou")
            return True

    return False


# Execucao principal comeca aqui
if __name__ == "__main__":
    while game_alive():
        line = 0
        col = 0

        if player_turn == "X":
            line, col = play_player_turn()
        else:
            line, col = play_pc_turn()

        table[line][col] = player_turn
        print(f"Jogada Efetuada na posicao ({line}, {col})")

        print()
        display_game_table()

        win_game = display_win_game()

        if win_game:
            break

        player_turn = "O" if player_turn == "X" else "X"

    if not win_game:
        print("Empate!")
