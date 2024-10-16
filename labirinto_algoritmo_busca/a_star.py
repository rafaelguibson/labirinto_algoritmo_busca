from pyamaze import maze, agent
from queue import PriorityQueue

destino = (30, 30)

def h_score(celula, destino):
    linha_atual = celula[0]
    coluna_atual = celula[1]
    linha_destino = destino[0]
    coluna_destino = destino[1]
    return abs(coluna_atual - coluna_destino) + abs(linha_atual - linha_destino)

def a_star(labirinto):
    # Criar um tabuleiro com f_score infinito
    f_score = {celula: float("inf") for celula in labirinto.grid}
    g_score = {}
    celula_inicial = (labirinto.rows, labirinto.cols)
    # Calcular o valor da célula inicial
    g_score[celula_inicial] = 0
    f_score[celula_inicial] = g_score[celula_inicial] + h_score(celula_inicial, destino)
    print(f_score)

    fila = PriorityQueue()
    item = (f_score[celula_inicial], h_score(celula_inicial, destino), celula_inicial)
    fila.put(item)

    while not fila.empty():
        celula = fila.get()
        if celula == destino:
            break
        for direcao in "NSEW":
            if labirinto.maze_map[celula][direcao] == 1:
                linha_celula = celula[0]
                coluna_celula = celula[1]
                if direcao == "N":
                    proxima_celula = (linha_celula - 1, coluna_celula)
                elif direcao == "S":
                    proxima_celula = (linha_celula + 1, coluna_celula)
                elif direcao == "W":
                    proxima_celula = (linha_celula, coluna_celula - 1)
                elif direcao == "E":
                    proxima_celula = (linha_celula, coluna_celula + 1)
                novo_g_score = g_score[celula] + 1
                novo_f_score = novo_g_score + h_score(proxima_celula, destino)

                if novo_g_score < f_score[proxima_celula]:
                    f_score[proxima_celula] = novo_f_score
                    g_score[proxima_celula] = novo_g_score
                    item = (novo_f_score, h_score(proxima_celula, destino), proxima_celula)
                    fila.put(item)

    # Caminhar a partir da celula inicial, explorando os proximos caminhos
        # Para cada possibilidade de caminho
            # Se o caminho é possivel (sem parede)
            # Se o f_score calculado < f_score do caminho antigo
                # Substituir o f_score antigo pelo calculado
                # Escolher o caminho para seguir que tem:
                    # O menor f_score
                    # Se os f_scores forem iguais, o que tem menor h_score
    caminho = ""
    return caminho


labirinto = maze(20,20)

labirinto.CreateMaze(loadMaze="maze--2024-10-16--09-58-35.csv")

caminho = a_star(labirinto)
agente = agent(labirinto, filled=True, footprints=True)
labirinto.tracePath({agente:caminho}, delay=150)
labirinto.run()
