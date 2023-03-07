from random import randint

# X = vez do jogador | O = vez do PC
player_turn = "X"

# -1 = Disponível o espaço | 0 = PC jogou na posicao
# 1 = Jogador jogou na posicao
table = [
    ["_", "_", "_"],
    ["_", "_", "_"],
    ["_", "_", "_"]
]

win_game = False

def game_alive():
    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j] == "_":
                return True
    
    return False

def display_game_table():
    for i in range(len(table)):
        print(table[i][0], table[i][1], table[i][2], sep=" | ")

def is_valid_position(line, col):
    if line < 0 or line > 2:
        return False
    
    if col < 0 or col > 2:
        return False

    if table[line][col] == "_":
        return True
    else:
        return False

# "X" Se for jogador ou "O" se for o PC
def verify_win_game(player):
    # Verificacao na horizontal = X X X
    for i in range(len(table)):
        if table[i][0] == player and \
           table[i][1] == player and \
           table[i][2] == player:
            return True
    
    # Verificacao na vertical
    for i in range(len(table)):
        if table[0][i] == player and \
           table[1][i] == player and \
           table[2][i] == player:
            return True

    # Verifica na diagonal
    if (table[0][0] == player and \
        table[1][1] == player and \
        table[2][2] == player) or \
        (table[0][2] == player and \
        table[1][1] == player and \
        table[2][0] == player):
        return True

    return False

# Execucao principal comeca aqui
if __name__ == "__main__":
    while game_alive():
        if player_turn == "X":
            line = int(input("Informe  um valor para a linha: "))
            col = int(input("Informe  um valor para a coluna: "))

            while not is_valid_position(line, col):
                print("Posicao nao e valida, amigao. Tente novamente")
                line = int(input("Informe  um valor para a linha: "))
                col = int(input("Informe  um valor para a coluna: "))
        else:
            line = randint(0, 2)
            col = randint(0, 2)

            while not is_valid_position(line, col):
                line = randint(0, 2)
                col = randint(0, 2)
        

        table[line][col] = player_turn
        print(f"Jogada Efetuada na posicao ({line}, {col})")
        
        print()
        # Exibir a situacao atual
        display_game_table()
        
        if verify_win_game(player_turn):
            win_game = True
            if player_turn == "X":
                print("Jogador ganhou")
                break;
            else:
                print("PC Ganhou")
                break;

        player_turn = "O" if player_turn == "X" else "X"

    if not win_game:
        print("Empate!")