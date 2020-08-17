from turtle import *


pedro = Turtle(visible=False)
matriz = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1,
    0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0,
    0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0,
    0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
    0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0,
    0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1,
    0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1,
    0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0,
    0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0,
]
def ler_matriz(matriz):
    # IMPLEMENTE A LÓGICA A SEGUIR
    return matriz # uma matriz fixa

def desenhar_celula(coordenada, cor='grey'):
    """ Dada uma coordenada (xt, yt) do Turtle, desenha um quadrado (célula) na posição """
    # IMPLEMENTE A LÓGICA ESPECIFICADA AQUI
    pedro.color(cor)
    pedro.speed(0)
    pedro.up()
    pedro.goto(coordenada)
    pedro.down()
    pedro.begin_fill()

    for i in range(4):
        pedro.forward(20)
        pedro.left(90)

    pedro.end_fill()

def em_coord_turtle(matriz):
    """ Dada uma coordenada da matriz (i,j) transforma em coordenada Turtle """
    # IMPLEMENTE A LÓGICA ESPECIFICADA AQUI
    # 'i' representa a linha e 'j' a coluna
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
    bgcolor('black')
    setup(p1, p2, p3, p4)
    # IMPLEMENTE A LÓGICA A SEGUIR
    # Para cada celula (i,j) da matriz que for caminho desenhe uma celula
    ler_matriz(matriz)
    coords = em_coord_turtle(matriz)
    for cod in coords:
        desenhar_celula(cod)
      
def main():
    criar_labirinto()
    done()

main()
