from pyamaze import maze,agent,textLabel,COLOR
from collections import deque

def bfs(labirinto, inicio=None):
    if inicio is None:
        inicio=(labirinto.rows, labirinto.cols)
    pontas = deque()
    pontas.append(inicio)
    caminho_bfs = {}
    explorado = [inicio]
    rota =[]
    proxima_celula = ()
    while len(pontas)>0:
        celula_atual = pontas.popleft()
        if celula_atual==labirinto._goal:
            break
        for d in 'ESNW':
            if labirinto.maze_map[celula_atual][d]:
                if d=='E':
                    proxima_celula=(celula_atual[0],celula_atual[1]+1)
                elif d=='W':
                    proxima_celula=(celula_atual[0],celula_atual[1]-1)
                elif d=='S':
                    proxima_celula=(celula_atual[0]+1,celula_atual[1])
                elif d=='N':
                    proxima_celula=(celula_atual[0]-1,celula_atual[1])
                if proxima_celula in explorado:
                    continue
                pontas.append(proxima_celula)
                explorado.append(proxima_celula)
                caminho_bfs[proxima_celula] = celula_atual
                rota .append(proxima_celula)
    melhor_caminho ={}
    celula=labirinto._goal
    while celula!=(labirinto.rows, labirinto.cols):
        melhor_caminho [caminho_bfs[celula]]=celula
        celula=caminho_bfs[celula]
    return rota ,caminho_bfs,melhor_caminho

if __name__=='__main__':

    labirinto=maze(12, 10)

    labirinto.CreateMaze(theme=COLOR.dark, loadMaze="maze--2024-10-16--14-52-19.csv")

    bSearch,bfsPath,fwdPath=bfs(labirinto)
    a=agent(labirinto, footprints=True, color=COLOR.cyan, shape='square', filled=True)
    b=agent(labirinto, footprints=True, color=COLOR.black, shape='arrow', filled=False)
    # c=agent(labirinto, 1, 1, footprints=True, color=COLOR.green, shape='square', filled=True, goal=(labirinto.rows, labirinto.cols))

    labirinto.tracePath({a:bSearch}, delay=50)
    # labirinto.tracePath({c:bfsPath}, delay=50)
    labirinto.tracePath({b:fwdPath}, delay=50)

    # Exibir o label com o tamanho do caminho
    l = textLabel(labirinto, 'Tamanho do caminho mais curto (BSF): ', len(fwdPath) + 1)

    labirinto.run()