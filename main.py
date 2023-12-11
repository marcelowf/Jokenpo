# Importações
from random import randint
from time import sleep

# Resultados possíveis
matriz = ["Pedra", "Papel", "Tesoura"]

# Função para obter a jogada do jogador
def obter_jogada(jogador):
    jogada = int(input(f"Jogador {jogador}, escolha sua jogada (1 - Pedra, 2 - Papel, 3 - Tesoura): "))
    while jogada not in [1, 2, 3]:
        jogada = int(input("Jogada inválida. Escolha novamente (1 - Pedra, 2 - Papel, 3 - Tesoura): "))
    return jogada

# Função para realizar a jogada do computador
def jogada_computador():
    return randint(1, 3)

# Função para determinar o resultado do jogo
def resultado(jogador1, jogador2):
    if jogador1 == jogador2:
        return "EMPATE!"
    elif (jogador1 == 2 and jogador2 == 1) or (jogador1 == 1 and jogador2 == 3) or (jogador1 == 3 and jogador2 == 2):
        return "JOGADOR 1 GANHOU!"
    else:
        return "JOGADOR 2 GANHOU!"

# Função principal do jogo
def jogar_jokenpo():
    print("JOKENPO!!!")
    sleep(0.5)

    while True:
        print("=-" * 25)
        print("QUAL MODALIDADE VOCÊ ESCOLHE PARA JOGAR?")
        print("1 = Usuário X Usuário")
        print("2 = Usuário X Computador")
        print("3 = Computador X Computador")
        modalidade = int(input("Resposta: "))

        while modalidade not in [1, 2, 3]:
            modalidade = int(input("Resposta inválida. Insira um valor válido: "))

        if modalidade == 1:
            jogada1 = obter_jogada(1)
            jogada2 = obter_jogada(2)
        elif modalidade == 2:
            jogada1 = obter_jogada(1)
            jogada2 = jogada_computador()
        else:
            jogada1 = jogada_computador()
            jogada2 = jogada_computador()

        print(f"O Jogador 1 jogou: {matriz[jogada1-1]} e o Jogador 2 jogou: {matriz[jogada2-1]}")
        sleep(0.5)
        print("=-" * 25)
        print(resultado(jogada1, jogada2))

        escolha = int(input("Deseja continuar jogando?\n{1} = Sim   {2} = Não\nEscolha: "))
        while escolha not in [1, 2]:
            escolha = int(input("Resposta inválida. Insira um valor válido: "))

        if escolha == 2:
            print("Muito obrigado por jogar meu jogo!")
            sleep(3)
            break
        else:
            sleep(1)
            print("Reiniciando...")
            sleep(2)

# Execução do jogo
jogar_jokenpo()
