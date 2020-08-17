from turtle import * # IMPORTA A BIBLIOTECA TURTLE


pedro = Turtle(visible=False) # TARTARUGA QUE VAI DESENHAR AS CÉLULAS

matriz = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0],
    [0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
]
def ler_matriz(matriz):
    # A PARTIR DE UMA MATRIZ BIDIMENSIONAL (LISTA DE LISTAS), DE TAMANHO 20x20, RETORNA UMA LISTA SÓ
    matriz_lida = []
    for linha in matriz:
        for coluna in linha:
            j = linha[coluna]
            matriz_lida.append(j)
    return matriz_lida 

def desenhar_celula(coordenada, cor='grey'):
    """ Dada uma coordenada (xt, yt) do Turtle, desenha um quadrado (célula) na posição """
    pedro.color(cor) # A TARTARUGA RECEBE POR PADRÃO A COR CINZA, MAS PODE SER ALTERADA
    pedro.speed(0)
    pedro.up()
    pedro.goto(coordenada) # VAI ATÉ A COORDENADA, QUE É PASSADA EM FORMATO DE TUPLA
    pedro.down()
    pedro.begin_fill()

    for i in range(4):
        pedro.forward(20) # DESENHA QUADRADOS DE TAMANHO 20x20
        pedro.left(90)

    pedro.end_fill()

def em_coord_turtle(matriz):
    """ Dada uma coordenada da matriz (i,j) transforma em coordenada Turtle """
    # RECEBE UMA LISTA COM OS VALORES DA MATRIZ E TRANSFORMA EM UMA LISTA COM COORDENADAS DE SEUS RESPECTIVOS VALORES
    celula = []
    coords = []
    for index in range(len(matriz)):
        celula.append(matriz[index])
         
        if matriz[index] == 1:
            x = (index % 20) * 20 - 200
            y = 180 - (index // 20) * 20
            c = x, y
            coords.append(c)
    return coords

def criar_labirinto(p1=420, p2=420, p3=370, p4=0):
    """ Cria uma tela do Turtle """
    bgcolor('black') # COR DE FUNDO PRETA
    setup(p1, p2, p3, p4)
    # IMPLEMENTE A LÓGICA A SEGUIR
    # Para cada celula (i,j) da matriz que for caminho desenhe uma celula
    matriz_lida = ler_matriz(matriz)
    coords = em_coord_turtle(matriz_lida)
    for cod in coords:
        desenhar_celula(cod)
      


def main():    
    criar_labirinto()
    done()
    
main()
