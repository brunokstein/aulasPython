import random

def jogar():

    print("*********************************")
    print("Bem vindo ao jogo de adivinhacao!")
    print("*********************************")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual nivel de dificuldade?")
    print("(1) Facil (2) Medio (3) Dificil")

    nivel = int(input("Define o nivel: "))
    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):

        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        chute = input("Digite um numero entre 1 e 100: ")
        numero = int(chute)
        print('Voce chutou:', numero)

        if(numero < 1 or numero > 100):
            print("Voce deve digitar um numero entre 1 e 100.")
            continue

        acertou = numero == numero_secreto
        chute_foi_maior = numero > numero_secreto
        chute_foi_menor = numero < numero_secreto

        if(acertou):
            print("Parabens, voce acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(chute_foi_maior):
                print("Voce errou! O seu chute foi maior do que o numero secreto!")
            elif(chute_foi_menor):
                print("Voce errou! O seu chute foi menor do que o numero secreto!")
            pontos_perdidos = abs(numero_secreto - numero)
            pontos = pontos - pontos_perdidos

        if(rodada == total_de_tentativas):
            print('O numero secreto era {}. Voce fez {} pontos!'.format(numero_secreto, pontos))

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()