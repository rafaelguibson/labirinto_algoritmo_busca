from pyamaze import maze, agent, COLOR, textLabel
from queue import PriorityQueue

destino = (1, 1)


def h_score(celula, destino):
    # Heristica de calculo por distancia Manhattan -> d = abs(x1 - x2) + abs(y1 - y2)
    # Distancia Euclidiana alternativa: e = sqrt(pow(x,2), pow(y,2))
    linha_atual, coluna_atual = celula
    linha_destino, coluna_destino = destino
    return abs(coluna_atual - coluna_destino) + abs(linha_atual - linha_destino)


def a_star(labirinto):

    f_score = {celula: float("inf") for celula in labirinto.grid}
    g_score = {}
    celula_inicial = (labirinto.rows, labirinto.cols)

    g_score[celula_inicial] = 0
    f_score[celula_inicial] = g_score[celula_inicial] + h_score(celula_inicial, destino)

    fila = PriorityQueue()
    fila.put((f_score[celula_inicial], h_score(celula_inicial, destino), celula_inicial))

    caminho = {}
    visitados = [celula_inicial]  # Lista para armazenar as células visitadas

    while not fila.empty():
        celula = fila.get()[2]
        if celula == destino:
            break
        proxima_celula = ()
        for direcao in "NSEW":
            if labirinto.maze_map[celula][direcao]:
                if direcao == "N":
                    proxima_celula = (celula[0] - 1, celula[1])
                elif direcao == "S":
                    proxima_celula = (celula[0] + 1, celula[1])
                elif direcao == "W":
                    proxima_celula = (celula[0], celula[1] - 1)
                elif direcao == "E":
                    proxima_celula = (celula[0], celula[1] + 1)

                novo_g_score = g_score[celula] + 1
                novo_f_score = novo_g_score + h_score(proxima_celula, destino)

                if novo_f_score < f_score[proxima_celula]:
                    f_score[proxima_celula] = novo_f_score
                    g_score[proxima_celula] = novo_g_score
                    fila.put((novo_f_score, h_score(proxima_celula, destino), proxima_celula))
                    caminho[proxima_celula] = celula
                    visitados.append(proxima_celula)  # Armazenar a célula visitada

    caminho_final = {}
    celula_analisada = destino
    while celula_analisada != celula_inicial:
        caminho_final[caminho[celula_analisada]] = celula_analisada
        celula_analisada = caminho[celula_analisada]

    return visitados, caminho_final

if __name__=='__main__':
    # Criação do Labirinto
    labirinto = maze()
    labirinto.CreateMaze(loopPercent=10, theme=COLOR.dark, loadMaze="maze--2024-10-16--14-52-19.csv")

    # Executar o algoritmo A*
    visitados, caminho = a_star(labirinto)

    # Adicionar agentes para mostrar células visitadas e caminho final
    agente_visitados = agent(labirinto, footprints=True, color=COLOR.blue, shape='square', filled=True)
    agente_caminho = agent(labirinto, footprints=True, color=COLOR.black, shape='arrow', filled=False)

    # Exibir as células visitadas e o caminho encontrado
    labirinto.tracePath({agente_visitados: visitados}, delay=50)
    labirinto.tracePath({agente_caminho: caminho}, delay=100)

    # Exibir o label com o tamanho do caminho
    l = textLabel(labirinto, 'Tamanho do caminho mais curto (A*): ', len(caminho) + 1)

    # Rodar o labirinto
    labirinto.run()
