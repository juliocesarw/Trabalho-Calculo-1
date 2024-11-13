
#CALCULAR A ALTURA MÁXIMA DE UM PROJÉTIL SABENDO A VELOCIDADE INICIAL (aleatório)  E O ÂNGULO ( 30,45,60 ) -> aleatorio
#CALCULAR A DISTÂNCIA PERCORRIDA PELO PROJÉTIL
#INSERIR UM JOGO PARA QUE O USUÁRIO INFORME UM POSSÍVEL VALOR DE DISTÂNCIA
#SE ACERTAR, GANHA PONTO
#PLOTAR O GRÁFICO

from random import randint
import math
import matplotlib
def gerar_numero_aleatorio():
    var = randint(1,10)
    return var

#VALOR RANDOMICO DO ANGULO E DA VELOCIDADE
def gerar_angulo():
    vetor = [30, 45, 60]
    angulo = randint(0,2)
    return (vetor[angulo]) 

def gerar_velocidade():
    velocidade = randint(1,100)
    return velocidade

#FUNÇÃO PARA CALCULAR A DISTANCIA
def distancia():
    velocidade = gerar_velocidade()
    angulo_aleatorio = gerar_angulo()
    angulo = math.radians(angulo_aleatorio)

    #mostrando na tela para possivel conferencia
    print("DADOS")
    print(f'velocidade: {velocidade}')
    print(f'angulo radiano: {angulo}')

    altura_maxima = pow(velocidade,2) * pow(math.sin(angulo), 2) / (2 * 9.8)
    return altura_maxima


################ PROGRAMA PRINCIPAL ####################
d = distancia()
print(d)

