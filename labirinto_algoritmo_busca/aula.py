from pyamaze import maze

labirinto = maze(30, 30) # é possivel passar argumentos rows e cols

#Create Maze também possui algumas personalizações por parametros

labirinto.CreateMaze()

#Mudar posição destino final do labirinto
# labirinto.CreateMaze(5,5)

# Salva um labirinto
# labirinto.CreateMaze(saveMaze=True)


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

#Executa o labirinto
labirinto.run()