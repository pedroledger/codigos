from turtle import * # IMPORTA A BIBLIOTECA TURTLE
from utils import floor
from random import choice
import numpy as np



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

def criar_labirinto(matriz, p1=420, p2=420, p3=370, p4=0):
    """ Cria uma tela do Turtle """
    tracer(False)
    hideturtle()
    bgcolor('black')
    setup(p1, p2, p3, p4)
    # Para cada celula (i,j) da matriz que for caminho desenhe uma celula
    tam_matriz = len(matriz)
    for lin in range(tam_matriz):
        for col in range(tam_matriz):
            if (matriz[lin][col] == 1):
                xt, yt = em_coord_turtle(lin,col)
                desenhar_celula(xt, yt, 'blue')
                desenhar_pastilha(xt, yt)
                
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

def em_coord_turtle(lin, col):
    """ Dada uma coordenada da matriz (i,j) transforma em coordenada Turtle """
    meio = dim // 2
    x = (col - meio) * tam_celula
    y = (meio - lin) * tam_celula
    return x, y 

def chao_da_celula(x, y):
    """ Dadas coordenadas do Turtle (x,y), retorna as coordenadas do início de uma célula.
        Por exemplo, na celula da origem com tamanho 20, a coordenada Turtle (10,10)
        representa o meio da célula. A chamada de função 'chao_da_celula(10, 10)' retorna
        as coordenadas de início dessa célula (0,0
        Dica: para entender, veja o exemplo da função: 'uso_do_floor()''
    """
    tam_celula = 20
    chao_x = int(floor(x, tam_celula))
    chao_y = int(floor(y, tam_celula))
    return chao_x, chao_y   

def adicionar_agente():
    """ Desenha o agente no labirinto """
    #dim = len(matriz)
    lin, col = cel_aleatoria(matriz)
    x, y = em_coord_turtle(lin, col)
    #if eh_caminho(x,y,matriz):
    desenhar_agente(x, y, 'yellow')

def em_coord_matriz(x, y):
    """ Dada uma coordenada do Turtle (x,y), retorna os índices correspondentes da matriz
        Por exemplo, numa matriz quadrada de dimensão 20, com tamanho de célula 20,
        a chamada de função 'em_coord_matriz(-200, 200)' deve retornar (0,0) e a
        chamada de função 'em_coord_matriz(0, 0)' deve retornar (10,10).
        Dica: utilize a função 'chao_da_celula(x, y)'
    """
    # IMPLEMENTE ESSA FUNÇÃO
    x, y = chao_da_celula(x,y)
    xm = (200 - y) // 20
    ym = (-200 + (-x)) // -20
    return xm, ym

def ler_matriz_aleatoria(dim):
    """ Retorna uma matriz quadrada na dimensão especificada com números
        aleatórios (0's e 1's)
        Dica: utilize numpy.random.randint()
    """
    matriz_aleatoria = []
    for i in range(dim):
        matriz_aleatoria.append([]*dim)
    for lin in matriz_aleatoria:
        for i in range(dim):
            lin.append(np.random.randint(0,2))
    # IMPLEMENTE ESSA FUNÇÃO
    return matriz_aleatoria

def cel_aleatoria(matriz):
    """ Retorna os índices de uma posição que contenha 1
        Por exemplo, na matriz a seguir:
        [[ 1  0  0 ]
         [ 0  1  0 ]
         [ 0  0  1 ]]
        Somente os elementos da diagonal principal [(0,0), (1,1), (2,2)]
        poderiam ser retornados
        Dica: utilize numpy.random.randint()
    """
    celulas = []
    for lin in range(len(matriz)):
        for col in range(len(matriz)):
            if matriz[lin][col] == 1:
                celulas.append((lin, col))
               
    aleat = choice(celulas)
    return aleat

def eh_caminho(lin, col, matriz):
    """ Dada uma matriz quadrada, retorna True quando (lin, col) == 1 e
        False caso contrário.
        Por exemplo, na matriz a seguir:
        [[ 1  0  0 ]
         [ 0  1  0 ]
         [ 0  0  1 ]]
        a chamada de função 'eh_caminho(0,0,matriz)' retorna True e
        a chamada de função 'eh_caminho(0,1,matriz)' retorna False
    """
    for lin in range(len(matriz)):
        for col in range(len(matriz)):
            if matriz[lin][col] == 1:
                return True
            else:
                return False

def desenhar_agente(x, y, cor):
    """ Leva a tartaruga até a posição (x,y) e desenha por exemplo um círculo
        para representar o agente (i.e., pacman, fantasmas)
    """
    up()
    goto(x+10, y+10)
    down()
    dot(20, cor)

def desenhar_pastilha(x, y, cor='white'):
    """ Leva a tartaruga até a posição (x,y) e desenha por exemplo um círculo
        para representar a pastilha
    """
    up()
    goto(x+10, y+10)
    down()
    dot(5, cor)


matriz = ler_matriz_aleatoria(20)
dim = len(matriz)
tam_celula = dim
tam_agente = dim

def teste1_transf_coord_funcionou():
    """ Testa as transformações de coordenadas """
    for lin in range(dim):
        for col in range(dim):
            x, y = em_coord_turtle(lin, col)
            if ( not (lin, col) == em_coord_matriz(x, y) ):
                return False
    return True

def teste2_transf_coord_funcionou():
    """ Testa as transformações de coordenadas """
    meio = dim // 2
    tam_celula = 20
    n = meio * tam_celula * 10
    for k1 in range(-n, n,5):
        for k2 in range(n, -n, -5):
            x = k1 / 10
            y = k2 / 10
            lin, col = em_coord_matriz(x, y)
            if (not chao_da_celula(x, y) == em_coord_turtle(lin, col) ):
                return False
    return True

def testar_transf_de_coord():
    """ Roda os testes de transformações de coordenadas """
    if (teste1_transf_coord_funcionou() and \
        teste2_transf_coord_funcionou()):
        return "Todas as transformações de coordenadas funcionaram"
    else:
        return "As transformações de coordenadas não funcionaram"

def main():
    criar_labirinto(matriz)
    adicionar_agente()
    done()
    
    print(testar_transf_de_coord())

main()
