from random import randint

def gerar_numero_aleatorio():
    var = randint(1,10)
    return var

def gerar_angulo():
    vetor = [30, 45, 60]
    angulo = randint(0,2)
    return vetor[angulo]

def menu():
    print("O que você quer saber?")
    print("[1] - Valor das raízes")
    print("[2] - Valor máximo")
    print("[3] - Valor das mínimo")
    print("[4] - Valor das raízes")
    print("[5] - Valor das raízes")

#principal

var = gerar_angulo()
print(var)

#PRINCIPAL