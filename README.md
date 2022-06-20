# Jokenpo
#game
#import´s
from random import randint
from time import sleep
#resultados
matriz = [[0], ["Pedra"], ["Papel"], ["Tesoura"]]
def resultado(a, b):
    if a == 2 and b == 1 or a == 1 and b == 3 or a == 3 and b == 2:
        return print("O JOGADOR 1 GANHOU!")
    elif a == b:
        return print("EMPATE!")
    else:
        return print("O JOGADOR 2 GANHOU!")
# apresentação para o usuário
contador = 0
print("JOKENPO!!!")
sleep(0.5)
while contador == 0:
    print("=-" * 25)
    print("""QUAL MODALIDADE VOCÊ ESCOLHE PARA JOGAR?
1 = Usuário X Usuário
2 = Usuário X Computador
3 = Computador X Computador""")
    modalidade = int(input("resposta: "))
    while modalidade > 3 or modalidade < 1:
        modalidade = int(input("resposta invalida, insira um valor valido: "))
        print("""JOGADAS POSSIVEIS:
1 = Pedra
2 = Papel
3 = Tesoura""")
    if modalidade == 1:
        a = int(input("jogador 1 escolha sua jogada: "))
        while a > 3 or a < 1:
            a = int(input("jogador 1 escolha sua jogada: "))
        b = int(input("jogador 2 escolha sua jogada: "))
        while b > 3 or b < 1:
            b = int(input("jogador 2 escolha sua jogada: "))
        print("o jogador 1 jogou:", matriz[a],"e o jogador 2 jogou:",matriz[b])
        sleep(0.5)
        print("=-" * 25)
        resultado(a, b)
    elif modalidade == 2:
        a = int(input("escolha sua jogada: "))
        while a > 3 or a < 1:
            a = int(input("jogador 1 escolha sua jogada: "))
        b = randint(1, 3)
        print("o jogador 1 jogou:", matriz[a],"e o jogador 2 jogou:",matriz[b])
        sleep(0.5)
        print("=-" * 25)
        resultado(a, b)
    else:
        a = randint(1, 3)
        b = randint(1, 3)
        print("o jogador 1 jogou:", matriz[a],"e o jogador 2 jogou:",matriz[b])
        sleep(0.5)
        print("=-" * 25)
        resultado(a, b)
    escolha = int(input("""Deseja continuar jogando?
{1} = sim   {2} = não 
escolha: """))
    while escolha > 2 or escolha < 1:
        escolha = int(input("resposta invalida, insira um valor valido: "))
    if escolha == 1:
        sleep(1)
        print("reniciando...")
        sleep(2)
    else:
        contador += 1
print("Muito obrigado por jogar meu jogo!")
sleep(3)
