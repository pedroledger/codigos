from turtle import * # IMPORTA A BIBLIOTECA TURTLE
from utils import vector
from random import choice



def ler_matriz():
    return [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

def criar_labirinto(p1=420, p2=420, p3=370, p4=0):
    """ Cria uma tela do Turtle """
    tracer(False)
    hideturtle()
    bgcolor('black')
    setup(p1, p2, p3, p4)
    # Para cada celula (i,j) da matriz que for caminho desenhe uma celula
    matriz = ler_matriz()
    tam_matriz = len(matriz)
    coordenadas_validas = []
    for lin in range(tam_matriz):
        for col in range(tam_matriz):
            if (matriz[lin][col] == 1):
                xt, yt = em_coord_turtle(lin,col)
                desenhar_celula(xt, yt, 'blue')
                goto(xt+10, yt+10)
                dot(5, 'white')
                coordenadas_validas.append(vector(xt, yt))
    pacman = choice(coordenadas_validas)
    up()
    goto(pacman.x +10, pacman.y+10)
    down()
    dot(20, 'yellow')
    update()

def desenhar_celula(xt, yt, cor='grey'):
    """ Dada uma coordenada (xt, yt) do Turtle, desenha um quadrado (célula) na posição """
    color(cor)
    up()
    goto(xt,yt)
    down()
    begin_fill()
    for _ in range(4):
        forward(20)
        left(90)
    end_fill()
    up()

def em_coord_turtle(xm, ym):
    """ Dada uma coordenada da matriz (i,j) transforma em coordenada Turtle """
    meio = 20 // 2
    yt = (ym - meio) * 20
    xt = (meio - xm) * 20
    return yt, xt    

def main():
    criar_labirinto()
    done()

main()