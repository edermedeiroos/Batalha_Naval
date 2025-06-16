import random

def criar_tabuleiro(tamanho, navios):
    tabuleiro = [[' - ' for _ in range(tamanho)]for _ in range(tamanho)] # Empty board creation

    for navio in navios:
        orientacao = random.choice(['HOR', 'VER']) # Boat orientation random choice

        if orientacao == 'VER':
            y = random.randint(0, 10 - navio['Celulas']) # Boat inicial y coordinate 
            x = random.randint(0, 9) # Boat inicial x coordinate

            while not verifica_posicoes(tabuleiro, y, x, quant=navio['Celulas'], orient=orientacao): # While any rand position is filled remake the coordinates
                y = random.randint(0, 10 - navio['Celulas'])
                x = random.randint(0, 9)

            for i in range(navio['Celulas']): # Executed when (y, x) coordinates finded are not filled
                tabuleiro[y + i][x] = ' O ' 

        else:
            x = random.randint(0, 10 - navio['Celulas']) # Boat inicial y coordinate 
            y = random.randint(0, 9) # Boat inicial x coordinate 

            while not verifica_posicoes(tabuleiro, y, x, quant=navio['Celulas'], orient=orientacao): # While any rand position is filled remake the coordinates
                x = random.randint(0, 10 - navio['Celulas'])
                y = random.randint(0, 9)

            for i in range(navio['Celulas']):
                tabuleiro[y][x + i] = ' O ' 

    return tabuleiro

def verifica_posicoes(mat, y, x, quant, orient):
    verificado = False

    if orient == 'VER':
        for posicao in mat[y: y+quant]: # Verify if any position in matrix y axis [y + quant] is already filled
            if posicao[x] == ' O ':
                verificado = False
                break
            verificado = True # If not filled, the verification became True

    else:
        for posicao in mat[y][x:x + quant]: # Verify if any position in matrix x axis [x + quant] is already filled
            if posicao == ' O ':
                verificado = False
                break
            verificado = True # If not filled, the verification became True
    
    return verificado

def visualizacao(tabuleiro): # Board Visualization
    print('     A,B,C,D,E,F,G,H,I,J'.replace(',', '   '))
    for indice, linha in enumerate(tabuleiro):
        if indice + 1 != 10:
            print(f'0{indice + 1} {linha}'.replace("'", "").replace(',', ''))
        else:
            print(f'{indice + 1} {linha}'.replace("'", "").replace(',', ''))

navios = [{'Navio': 'Porta-Avioes', 'Celulas': 5}, 
          {'Navio': 'Navio-de-Batalha', 'Celulas': 4},
          {'Navio': 'Cruzador', 'Celulas': 3},
          {'Navio': 'Destruidor1', 'Celulas': 2},
          {'Navio': 'Destruidor2', 'Celulas': 2},
          {'Navio': 'Submarino1', 'Celulas': 1},
          {'Navio': 'Submarino2', 'Celulas': 1}]

tabuleiro = criar_tabuleiro(10, navios)
visualizacao(tabuleiro)