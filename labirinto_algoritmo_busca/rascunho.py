from pyamaze import maze, agent

labirinto = maze(30, 30) # é possivel passar argumentos rows e cols

#Create Maze também possui algumas personalizações por parametros

labirinto.CreateMaze()

#Mudar posição destino final do labirinto
# labirinto.CreateMaze(5,5)

# Salva um labirinto
# Gera um arquivo CSV contendo a estrutura do labirinto
# labirinto.CreateMaze(saveMaze=True)

#Carregar um labirinto a partir de um CSV
# Sempre carregará o mesmo labirinto
# labirinto.CreateMaze(loadMaze="maze--2024-10-16--08-56-13.csv")

#LoopPercente é um parametro do CreateMaze para definir o numero de caminhos possivel para solucionar o labirinto
# Por padrão é zero, o que significa que ele so tem uma caminho possivel
# Aumentar o valor, aumenta o numero de soluções possiveis
# labirinto.CreateMaze(loopPercent=30)
#Printa as celulas do labirinto

celulas = labirinto.grid
print(celulas)

#Imprime um mapa do labirinto
# O mapa do labirinto é um dicionario aonde cada chave do dicionário é uma celula, e o valor é um outro dicionario com as 4 direções Norte, Sul, Leste, Oeste
# (Zero significa que existe uma parede naquela direção, e numero 1 indica que o caminha é livre naquela direção
mapa = labirinto.maze_map
print(mapa)

#Caminho do labirinto
# Diz o caminho perfeito que alguem teria que percorrer para chegar do ponto inicial ao ponto final
caminho = labirinto.path
print(caminho)

#O Agente pode receber parametros (x, y) da posicaão, filled para preencher tdo o quadrado e footprint exibe o "rastro" do deslocamento percorrido
agente = agent(labirinto, filled=True, footprints=True)

#mudar posição do agente manualmente
# agente.position = (30, 29)
# agente.position = (30, 28)

#Movendo o agente por um caminho
#O caminho pode ser passado no mesmo formato do mapa de posições
caminho = labirinto.path
#o trace path recebe um dicionario labirinto.tracePath({agente:caminho})
# Parametro delay ajusta o tempo da animação
labirinto.tracePath({agente:caminho}, delay=300)
#Executa o labirinto
labirinto.run()