from pyamaze import maze, agent

destino = (30, 30)

def h_score(celula, destino):
    linha_atual = celula[0]
    coluna_atual = celula[1]
    linha_destino = destino[0]
    coluna_destino = destino[1]
    return abs(coluna_atual - coluna_destino) + abs(linha_atual - linha_destino)

def a_star(labirinto):
    # Criar um tabuleiro com f_score infinito

    # Calcular o valor da célula inicial
    # Caminhar a partir da celula inicial, explorando os proximos caminhos
        # Para cada possibilidade de caminho
            # Se o caminho é possivel (sem parede)
            # Se o f_score calculado < f_score do caminho antigo
                # Substituir o f_score antigo pelo calculado
                # Escolher o caminho para seguir que tem:
                    # O menor f_score
                    # Se os f_scores forem iguais, o que tem menor h_score
    return caminho


labirinto = maze(20,20)

labirinto.CreateMaze(loadMaze="maze--2024-10-16--09-58-35.csv")

caminho = labirinto.path
agente = agent(labirinto, filled=True, footprints=True)
labirinto.tracePath({agente:caminho}, delay=150)
labirinto.run()
