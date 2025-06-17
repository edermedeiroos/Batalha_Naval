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

def visualizacao(tabuleiro): # Board Visualization
    print('     ', end='')
    for i in range(len(tabuleiro)): # Letters 
        print(chr(65+i), end='   ')
    print()

    for indice, linha in enumerate(tabuleiro): # Numbers
        if indice + 1 < 10:
            print(f'0{indice + 1} {linha}'.replace("'", "").replace(',', '')) 
        else:
            print(f'{indice + 1} {linha}'.replace("'", "").replace(',', ''))

navios = [{'Navio': 'Porta-Avioes', 'Celulas': 5}, # Boats name and size
          {'Navio': 'Navio-de-Batalha', 'Celulas': 4},
          {'Navio': 'Cruzador', 'Celulas': 3},
          {'Navio': 'Destruidor1', 'Celulas': 2},
          {'Navio': 'Destruidor2', 'Celulas': 2},
          {'Navio': 'Submarino1', 'Celulas': 1},
          {'Navio': 'Submarino2', 'Celulas': 1}]
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
    visualizacao(tabuleiro_jogador)
    visualizacao(tabuleiro_verdade)
    print(' '*50, f'JOGADAS RESTANTES: {tentativas + 1 - i}')

    while True: # Error verification
        try:
            jogada = str(input("Coordenada do Tiro [Coluna/Linha]: ")).upper() # Player's move
            linha = int(jogada[1:]) - 1 # Board Line
            coluna = int(ord(jogada[0]) - ord("A")) # Board Column

            if linha not in range(len(tabuleiro_verdade)) or coluna not in range(len(tabuleiro_verdade)):
                print("*TIRO FORA DOS LIMITES*") # Shot out of the range
                continue

            elif tabuleiro_jogador[linha][coluna] == ' X ':
                print("*TIRO REPETIDO*") # Repeated Shot
                continue

        except (ValueError, TypeError):
            print("*JOGADA INVÁLIDA*") # Invalid move (Usually switch between line and column)
            continue
        
        break

    if tabuleiro_verdade[linha][coluna] in letras_navios: # Shot verification
        print("ACERTOU!")
        tabuleiro_jogador[linha][coluna] = ' O ' # Player board update
    else:
        print("ERROU!")
        tabuleiro_jogador[linha][coluna] = ' X ' # Player board update

    # TODO refazer as letras do tabuleiro_jogador para verificar com tabuleiro_verdade
    if tabuleiro_jogador == tabuleiro_verdade: # Win condition
        print(" - VOCÊ GANHOU! - ")
        break

if tabuleiro_jogador != tabuleiro_verdade:
    print(" - VOCÊ PERDEU! - ")