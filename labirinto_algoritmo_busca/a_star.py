from pyamaze import maze, agent, COLOR
from queue import PriorityQueue

destino = (1, 1)

def h_score(celula, destino):
    linha_atual = celula[0]
    coluna_atual = celula[1]
    linha_destino = destino[0]
    coluna_destino = destino[1]
    return abs(coluna_atual - coluna_destino) + abs(linha_atual - linha_destino)

def a_star(labirinto):
    # Criar um tabuleiro com f_score infinito
    f_score = {celula: float("inf") for celula in labirinto.grid}
    # Criar Dicionário g_score
    g_score = {}
    # Calcular o valor da célula inicial
    celula_inicial = (labirinto.rows, labirinto.cols)
    g_score[celula_inicial] = 0
    f_score[celula_inicial] = g_score[celula_inicial] + h_score(celula_inicial, destino)
    # Definir fima de prioridade para controle dos caminhos
    fila = PriorityQueue()
    item = (f_score[celula_inicial], h_score(celula_inicial, destino), celula_inicial)
    fila.put(item)

    caminho = {}
    # Percorrer caminho utilizando a fila
    while not fila.empty():
        celula = fila.get()[2]

        if celula == destino:
            break

        for direcao in "NSEW":
            if labirinto.maze_map[celula][direcao] == 1:
                linha_celula = celula[0]
                coluna_celula = celula[1]
                # Calcular qual a proxima célula
                if direcao == "N":
                    proxima_celula = (linha_celula - 1, coluna_celula)
                elif direcao == "S":
                    proxima_celula = (linha_celula + 1, coluna_celula)
                elif direcao == "W":
                    proxima_celula = (linha_celula, coluna_celula - 1)
                elif direcao == "E":
                    proxima_celula = (linha_celula, coluna_celula + 1)
                # Calcular g_score e f_core da proxima celua
                novo_g_score = g_score[celula] + 1
                novo_f_score = novo_g_score + h_score(proxima_celula, destino)
                #Verificar se o caminho terá um menor custo
                if novo_f_score < f_score[proxima_celula]:
                    f_score[proxima_celula] = novo_f_score
                    g_score[proxima_celula] = novo_g_score
                    item = (novo_f_score, h_score(proxima_celula, destino), proxima_celula)
                    fila.put(item)
                    caminho[proxima_celula] = celula
    # Caminho da rota perfeita
    caminho_final = {}
    celula_analisada = destino
    while celula_analisada != celula_inicial:
        caminho_final[caminho[celula_analisada]] = celula_analisada  # invertendo chave e valor do dicionário caminho
        celula_analisada = caminho[celula_analisada]  # atualizando para a próxima célula analisada
    return caminho_final


labirinto = maze(30,30)

labirinto.CreateMaze()

caminho = a_star(labirinto)
agente = agent(labirinto, filled=True, footprints=True, color=COLOR.cyan)
labirinto.tracePath({agente:caminho}, delay=50)
labirinto.run()
