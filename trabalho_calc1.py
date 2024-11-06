
#CALCULAR A ALTURA MÁXIMA DE UM PROJÉTIL SABENDO A VELOCIDADE INICIAL (aleatório)  E O ÂNGULO ( 30,45,60 ) -> aleatorio
#CALCULAR A DISTÂNCIA PERCORRIDA PELO PROJÉTIL
#INSERIR UM JOGO PARA QUE O USUÁRIO INFORME UM POSSÍVEL VALOR DE DISTÂNCIA
#SE ACERTAR, GANHA PONTO
#PLOTAR O GRÁFICO

from random import randint

def gerar_numero_aleatorio():
    var = randint(1,10)
    return var

def gerar_angulo():
    vetor = [30, 45, 60]
    angulo = randint(0,2)
    return vetor[angulo]
def menu():
    print("MENU")
