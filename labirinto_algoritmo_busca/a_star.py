from pyamaze import maze, agent, COLOR, textLabel
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

def bfs(labirinto):
    inicio=(labirinto.rows, labirinto.cols)
    atual=[inicio]
    explorado=[inicio]
    bfs_caminho={}
    while len(atual)>0:
        celula_atual=atual.pop(0)
        if celula_atual==(1,1):
            break
        for d in 'ESNW':
            if labirinto.maze_map[celula_atual][d]:
                if d=='E':
                    proxima_celula =(celula_atual[0],celula_atual[1]+1)
                elif d=='W':
                    proxima_celula =(celula_atual[0],celula_atual[1]-1)
                elif d=='N':
                    proxima_celula =(celula_atual[0]-1,celula_atual[1])
                elif d=='S':
                    proxima_celula =(celula_atual[0]+1,celula_atual[1])
                if proxima_celula  in explorado:
                    continue
                atual.append(proxima_celula )
                explorado.append(proxima_celula )
                bfs_caminho[proxima_celula ]=celula_atual
    caminho_final={}
    celula=(1,1)
    while celula!=inicio:
        caminho_final[bfs_caminho[celula]]=celula
        celula=bfs_caminho[celula]
    return caminho_final


# Criação do Labirinto
labirinto = maze()

labirinto.CreateMaze(loadMaze="maze--2024-10-16--12-13-34.csv", theme=COLOR.dark)

# Definir qual algoritmo usar: 'a_star' ou 'bfs'
algoritmo_usado = 'a_star'  # Alterar para 'bfs' se quiser usar BFS

if algoritmo_usado == 'a_star':
    caminho = a_star(labirinto)
    label_texto = 'Tamanho do caminho mais curto encontrado no algoritmo A* : '
else:
    caminho = bfs(labirinto)
    label_texto = 'Tamanho do caminho mais curto encontrado no algoritmo BFS : '


# Adicionar agente e exibir o caminho
agente = agent(labirinto, filled=True, footprints=True, color=COLOR.red)
labirinto.tracePath({agente: caminho}, delay=50)

# Exibir o label com o texto correto
l = textLabel(labirinto, label_texto, len(caminho) + 1)
labirinto.run()
