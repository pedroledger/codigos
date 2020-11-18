from turtle import *
from matriz import Matriz

class Mercado:
    def __init__(self, tam_celula=None):
        """Construtor do Mercado"""

        if (not tam_celula): #se tamanho da celula não for passada, recebe 20
            self.tam_celula = 20
        else:
            self.tam_celula = tam_celula

    def criar_matriz(self):
        self.matriz = Matriz().ler_fixa()

    def criar_tela(self, p1=420, p2=420, p3=370, p4=0):
        """ Cria uma tela do Turtle """
        tracer(False)
        hideturtle()
        bgcolor('black')
        setup(p1, p2, p3, p4)
        #self.criar_planta_mercado()

    def criar_planta_mercado(self):
        setup(420, 420, 370, 0)

        
