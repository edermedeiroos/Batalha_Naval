import random

def criar_tabuleiro(tamanho, navios=''):
    tabuleiro = [[' - ' for _ in range(tamanho)]for _ in range(tamanho)] # Empty board creation

    for navio in navios:
        letra_navio = navio['Navio'][0]
        orientacao = random.choice(['HOR', 'VER']) # Boat orientation random choice

        if orientacao == 'VER':
            y = random.randint(0, 10 - navio['Celulas']) # Boat inicial y coordinate
            x = random.randint(0, 9) # Boat inicial x coordinate

            while not verifica_posicoes(tabuleiro, y, x, navio['Celulas'], orientacao): # While any rand position is filled remake the coordinates
                y = random.randint(0, 10 - navio['Celulas'])
                x = random.randint(0, 9)

            for i in range(navio['Celulas']): # Executed when (y, x) coordinates finded are not filled
                tabuleiro[y + i][x] = f' {letra_navio} '

        else:
            x = random.randint(0, 10 - navio['Celulas']) # Boat inicial y coordinate
            y = random.randint(0, 9) # Boat inicial x coordinate

            while not verifica_posicoes(tabuleiro, y, x, navio['Celulas'], orientacao): # While any rand position is filled remake the coordinates
                x = random.randint(0, 10 - navio['Celulas'])
                y = random.randint(0, 9)

            for i in range(navio['Celulas']):
                tabuleiro[y][x + i] = f' {letra_navio} '

    return tabuleiro

def verifica_posicoes(mat, y, x, quant, orient):
    verificado = False

    if orient == 'VER':
        for posicao in mat[y: y+quant]: # Verify if any position in matrix y axis [y + quant] is already filled
            if posicao[x] in letras_navios: # Verify if position == any boat letter
                verificado = False
                break
            verificado = True # If not filled, the verification became True

    else:
        for posicao in mat[y][x:x + quant]: # Verify if any position in matrix x axis [x + quant] is already filled
            if posicao in letras_navios: # Verify if position == any boat letter
                verificado = False
                break
            verificado = True # If not filled, the verification became True

    return verificado

def visualizacao(tabuleiro, esconder = True): # Board Visualization
    def formatacao(string, esconder_nome = True):
        if esconder_nome:
            print(string.replace("'", "").replace(",", "").replace("P", "O").replace("N", "O").replace("C", "O").replace("D", "O").replace("S", "O"))
        else:
            print(string.replace("'", "").replace(",", ""))

    print('     ', end='')
    for i in range(len(tabuleiro)): # Letters
        print(chr(65+i), end='   ')
    print()
    for indice, linha in enumerate(tabuleiro): # Numbers
        if indice + 1 < 10:
            formatacao(f'0{indice + 1} {linha}', esconder_nome=esconder)
        else:
            formatacao(f'{indice + 1} {linha}', esconder_nome=esconder)

def contador_barcos(tabuleiro, navios):
    navios_destruidos = 0 
    set_navios = navios.copy() 

    for navio in set_navios: # Remove repeted boat's
        if set_navios.count(navio) > 1:
            set_navios.remove(navio)

    for navio in set_navios: # Counter += 1 if tabuleiro.count letter is a Boat's size multiple
        navios_destruidos += (str(tabuleiro).count(navio["Navio"][0]))//(navio["Celulas"])

    return(navios_destruidos)

navios = [{'Navio': 'Porta-Avioes', 'Celulas': 5}, # Boats name and size
          {'Navio': 'Navio-de-Batalha', 'Celulas': 4},
          {'Navio': 'Cruzador', 'Celulas': 3},
          {'Navio': 'Destruidor', 'Celulas': 2},
          {'Navio': 'Destruidor', 'Celulas': 2},
          {'Navio': 'Submarino', 'Celulas': 1},
          {'Navio': 'Submarino', 'Celulas': 1}]
letras_navios = [f' {navio["Navio"][0]} ' for navio in navios] # Boats inicial letter

tabuleiro_verdade = criar_tabuleiro(10, navios) # Board with boats
tabuleiro_jogador = criar_tabuleiro(10) # Board with hidden boats

print('-'*15, 'BATALHA NAVAL', '-'*15, end='\n\n')
print(' - NÚMERO DE TENTATIVAS - ')
print('50 (FÁCIL) | 42 (MÉDIO) | 35 (DIFÍCIL)', end='\n\n')

while True: # Difficult mode choice
    try:
        tentativas = int(input('- Opcão: '))
        if tentativas not in [50, 42, 35]:
            raise IndexError
        break

    except (ValueError, TypeError):
        print("*Digite apenas números*", end='\n\n')

    except IndexError:
        print("*Modo de jogo desconhecido*", end='\n\n')

for i in range(1, tentativas + 1): # Game
    visualizacao(tabuleiro_jogador, esconder=True)
    # visualizacao(tabuleiro_verdade, esconder=False)
    print(' '*10, f'| JOGADAS RESTANTES: {tentativas + 1 - i} |')
    print(' '*10, f'| BARCOS DESTRUIDOS: {contador_barcos(tabuleiro_jogador, navios)}  |')
    print()

    while True: # Player's move and Error verification
        try:
            jogada = str(input("- Coordenada do Tiro [Coluna/Linha]: ")).upper() # Player's move
            linha = int(jogada[1:]) - 1 # Board Line
            coluna = int(ord(jogada[0]) - ord("A")) # Board Column

            if linha not in range(len(tabuleiro_verdade)) or coluna not in range(len(tabuleiro_verdade)):
                print("*TIRO FORA DOS LIMITES*", end='\n\n') # Shot out of the range
                continue

            elif tabuleiro_jogador[linha][coluna] == ' X ' or tabuleiro_jogador[linha][coluna] in letras_navios:
                print("*TIRO REPETIDO*", end='\n\n') # Repeated Shot
                continue

        except (ValueError, TypeError):
            print("*JOGADA INVÁLIDA*", end='\n\n') # Invalid move (Usually switch between line and column)
            continue

        break

    if tabuleiro_verdade[linha][coluna] in letras_navios: # Shot verification
        print("ACERTOU!", end='\n\n')
        tabuleiro_jogador[linha][coluna] = tabuleiro_verdade[linha][coluna] # Player board update
    else:
        print("ERROU!", end='\n\n')
        tabuleiro_jogador[linha][coluna] = ' X ' # Player board update

    if contador_barcos(tabuleiro_jogador, navios) == len(navios): # Win condition
        print(" - VOCÊ GANHOU! - ")
        break

if contador_barcos(tabuleiro_jogador, navios) != len(navios): # Defeat condition
    print(" - VOCÊ PERDEU! - ")
    print(f'\n - GABARITO DOS BARCOS: \n')
    visualizacao(tabuleiro_verdade, esconder=True)